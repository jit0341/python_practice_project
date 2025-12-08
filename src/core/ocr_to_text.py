import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path):
    # Load image
    image = Image.open(image_path)

    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text.strip()

def save_text_to_file(text, output_file='ocr_output.txt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"[✅] Extracted text saved to {output_file}")

if __name__ == "__main__":
    img_path = input("Enter image file path (e.g., test.png): ").strip()

    if not os.path.exists(img_path):
        print("[❌] File does not exist!")
    else:
        text = extract_text_from_image(img_path)
        print("\n[📝] Extracted Text:\n")
        print(text)
        save_text_to_file(text)
