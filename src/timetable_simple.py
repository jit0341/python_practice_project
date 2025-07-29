from PIL import Image
import pytesseract
import openpyxl
import pandas as pd # pandas is still very useful for data manipulation

# Load the image
image_path = "/storage/emulated/0/python_practice_project/src/IMG-20250721-WA0020.jpg"  # Your handwritten timetable image
img = Image.open(image_path)

# Perform OCR to get detailed data including bounding boxes
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

# Create a DataFrame from the OCR data
df = pd.DataFrame(data)

# Filter out empty text and confidence below a threshold
df = df[df.conf != -1] # Remove rows with no confidence (often empty)
df = df[df.text.astype(str).str.strip() != ''] # Remove rows with empty text or just spaces
df['text'] = df['text'].astype(str).str.strip() # Ensure text is string and stripped

#-- ADD THIS LINE TO PRINT COORDINATES ---
print("\n--- OCR Data (Text, Left, Top, Column ID, Row ID) ---")
# Print only relevant columns for easier reading
# Use .to_string() to avoid truncation
print(df[['text', 'left', 'top', 'width', 'height', 'conf']].to_string())
print("---------------------------------------------------\n")
# --- END ADDITION ---

# Sort by top (Y-coordinate) and then by left (X-coordinate) to roughly order the text
df = df.sort_values(by=['top', 'left']).reset_index(drop=True)

# ... (rest of your row and column detection logic) ...



# Sort by top (Y-coordinate) and then by left (X-coordinate) to roughly order the text
df = df.sort_values(by=['top', 'left']).reset_index(drop=True)

# --- Logic to identify rows ---
# A simple approach: assume a new row if the 'top' coordinate significantly increases
row_threshold = 10 # Adjust this value based on spacing in your timetable
current_row = 0
df['row_id'] = 0 # Initialize row_id column

if not df.empty:
    df.loc[0, 'row_id'] = current_row
    for i in range(1, len(df)):
        # Calculate vertical difference between current word and the median 'top' of the previous words in the same "logical line"
        # Using a fixed previous word's top is simpler for now, but median could be more robust
        if df.loc[i, 'top'] - df.loc[i-1, 'top'] > row_threshold:
            current_row += 1
        df.loc[i, 'row_id'] = current_row

# --- Logic to identify columns (Rule-based, no KMeans) ---
# This is more challenging and might require manual tuning or visual inspection of X-coordinates.
# We'll define approximate column boundaries based on your timetable's layout.
# You'll need to look at your image (1000078452.jpg) and estimate these.

# Example estimated column boundaries (left-most X-coordinate for each column).
# These are highly dependent on your image. You might need to adjust these by trial and error.
# Run the OCR without column logic first, print `df['left']` to get an idea of X-coordinates.

# Approximate X-coordinates for your columns based on the image (adjust as needed!)
# Column 1: Time (e.g., 0-100)
# Column 2: 3rd A (e.g., 100-250)
# Column 3: 3rd B (e.g., 250-400)
# Column 4: 4th B (e.g., 400-550)
# Column 5: 5th B (e.g., 550-700)
# Column 6: 5th A (e.g., 700-850)
# Column 7: (e.g., 850+) - for last column, if any

column_boundaries = [
    0,    # Start of column 0
    100,  # Start of column 1
    250,  # Start of column 2
    400,  # Start of column 3
    550,  # Start of column 4
    700,  # Start of column 5
      # Start of column 6
]
# If your table has 7 columns, this means we have 7 "bins".
# The number of boundaries should be `num_columns`.

# Assign column_id based on these boundaries
def assign_column_by_boundary(left_coord, boundaries):
    for i, boundary_start in enumerate(boundaries):
        if left_coord >= boundary_start:
            # Check if it's within the next boundary, or if it's the last boundary
            if i + 1 < len(boundaries):
                if left_coord < boundaries[i+1]:
                    return i
            else: # Last column
                return i
    return 0 # Default to the first column if somehow out of bounds (shouldn't happen with 0)


# If you need to estimate these boundaries, you can print the 'left' column of your DataFrame:
# print(df['left'].describe())
# print(df['left'].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]))
# And then manually set 'column_boundaries' based on clusters you see.
# For example, look at a row's 'left' values and see where the gaps are.

# Apply column assignment
if not df.empty:
    df['column_id'] = df['left'].apply(lambda x: assign_column_by_boundary(x, column_boundaries))
else:
    df['column_id'] = 0 # Fallback if df is empty

# Create an empty list of lists to represent the table
# Determine max row and column IDs
max_row = df['row_id'].max() if not df.empty else 0
max_col = df['column_id'].max() if not df.empty else 0

table_data = [['' for _ in range(max_col + 1)] for _ in range(max_row + 1)]

# Populate the table_data
for index, row in df.iterrows():
    r_idx = int(row['row_id'])
    c_idx = int(row['column_id'])
    text = row['text']

    if r_idx <= max_row and c_idx <= max_col:
        # Simple concatenation for text in the same "cell"
        if table_data[r_idx][c_idx] == '':
            table_data[r_idx][c_idx] = text
        else:
            # Append if there's already text, assuming it's part of the same cell
            table_data[r_idx][c_idx] += " " + text

# Create an Openpyxl workbook and write the data
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Timetable"

for r_idx, row_content in enumerate(table_data):
    for c_idx, cell_value in enumerate(row_content):
        ws.cell(row=r_idx + 1, column=c_idx + 1, value=cell_value)

# Save the Excel file
output_excel_path = "structured_timetable_no_ml.xlsx"
wb.save(output_excel_path)

print(f"✅ Attempted to save structured timetable to {output_excel_path}")
print("Please note: Manual review and correction of the Excel file may be necessary due to the nature of handwritten OCR and simplified column detection.")
print("If columns are misaligned, adjust 'column_boundaries' in the script.")

