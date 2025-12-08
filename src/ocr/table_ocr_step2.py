import cv2
import pytesseract

# Load image
image_path = input("Enter image path: ")
image = cv2.imread(image_path)

# Run OCR with position data
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

# Draw bounding boxes
for i in range(len(data['text'])):
    if int(data['conf'][i]) > 30 and data['text'][i].strip() != '':
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        text = data['text'][i]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

# Save the image with boxes
output_path = image_path.replace(".jpg", "_boxed.jpg")
cv2.imwrite(output_path, image)
print(f"✅ Image saved with boxes: {output_path}")
