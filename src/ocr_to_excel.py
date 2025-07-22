from PIL import Image
import pytesseract
import openpyxl

# Load image
img = Image.open("IMG-20250721-WA0020.jpg")

# OCR text
text = pytesseract.image_to_string(img)

# Create Excel workbook
wb = openpyxl.Workbook()
ws = wb.active

# Write each line to a new row
for i, line in enumerate(text.split('\n')):
    ws.cell(row=i+1, column=1, value=line.strip())

# Save
wb.save("timetable_output.xlsx")
print("✅ Saved to timetable_output.xlsx")
