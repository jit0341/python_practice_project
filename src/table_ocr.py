import pytesseract
from PIL import Image
import pandas as pd
import os

# 1. Load the image
image_path = input("Enter image file path(/storage/emulated/0/python_practice_project/src/IMG-20250721-WA0020.jpg): ")
image = Image.open(image_path)

# 2. Extract text using pytesseract
raw_text = pytesseract.image_to_string(image)

# 3. Process raw text to rows
rows = raw_text.strip().split('\n')
data = [row.split() for row in rows if row.strip()]  # crude column splitting

# 4. Save to Excel
df = pd.DataFrame(data)
output_file = os.path.splitext(os.path.basename(image_path))[0] + "_output.xlsx"
df.to_excel(output_file, index=False, header=False)

print(f"✅ Text saved to: {output_file}")
