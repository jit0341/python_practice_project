from PIL import Image
import pytesseract
import pandas as pd

# Step 1: Load your image
img_path = '/storage/emulated/0/python_practice_project/src/IMG-20250715-WA0003.jpg'  # Replace with your image name
img = Image.open(img_path)

# Step 2: Use image_to_data to get OCR + position info
ocr_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME)

# Step 3: Filter out empty text results
ocr_data = ocr_data[ocr_data['text'].notna()]
ocr_data = ocr_data[ocr_data['text'].str.strip() != '']

# Step 4: Display top rows
print(ocr_data[['left', 'top', 'width', 'height', 'text']].head(10))

# Optional: Save to CSV
ocr_data.to_csv("ocr_raw_data.csv", index=False)
