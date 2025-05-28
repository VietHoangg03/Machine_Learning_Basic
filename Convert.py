import fitz  # PyMuPDF
from PIL import Image
import os
import glob

def pdf_to_images(pdf_path, output_dir, max_pages=20):
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    for i in range(min(len(doc), max_pages)):
        page = doc[i]
        pix = page.get_pixmap(dpi=300)
        output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page{i+1}.png")
        pix.save(output_path)
    print(f"✅ Đã chuyển xong file {os.path.basename(pdf_path)}")

# Thư mục chứa các file PDF
input_dir = "/Users/mac/Documents/OCR/OCR_TRAINING/Thông báo tổ chức hội nghị, hội thảo, đào tạo về bán hàng đa cấp"
output_dir = os.path.join(input_dir, "Image")

# Tìm tất cả file PDF trong thư mục
pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))

# Chuyển đổi từng file PDF
for pdf_file in pdf_files:
    pdf_to_images(pdf_file, output_dir, max_pages=20)
