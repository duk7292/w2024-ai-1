from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def fileToTextData(file_path, dpi=300):
    """Extracts text data from an image or PDF and returns it as structured output."""
    allData = []
    
    if file_path.lower().endswith(".pdf"):
        images = convert_from_path(file_path, dpi=dpi)
    else:
        images = [Image.open(file_path)]
    
    for i, img in enumerate(images):
        print(f"Processing page {i + 1}...")
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        allData.append({"page": i + 1, "data": data})
    
    print("Text extraction complete.")
    return allData
