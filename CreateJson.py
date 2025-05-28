import os
import glob
import json

# Đường dẫn đến thư mục chứa ảnh PNG
input_dir = "/Users/mac/Documents/OCR/OCR_TRAINING_CONVERT/Cấp chứng chỉ hành nghề hoạt động xây dựng lần đầu hạng II, III/Image"

# Tạo thư mục Label nếu chưa tồn tại
label_dir = os.path.join(os.path.dirname(input_dir), "Label")
os.makedirs(label_dir, exist_ok=True)

# Tìm tất cả file PNG trong thư mục
png_files = glob.glob(os.path.join(input_dir, "*.png"))

# Đếm số file JSON mới được tạo
new_files_count = 0

# Tạo file JSON trống cho mỗi file PNG nếu chưa tồn tại và chỉ cho page1
for png_file in png_files:
    # Lấy tên file không có đuôi .png
    base_name = os.path.splitext(os.path.basename(png_file))[0]
    
    # Chỉ xử lý các file có chứa "page1"
    if "page1" in base_name:
        # Tạo đường dẫn cho file JSON mới
        json_path = os.path.join(label_dir, f"{base_name}.json")
        
        # Kiểm tra nếu file JSON chưa tồn tại thì mới tạo
        if not os.path.exists(json_path):
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump({
                    "messages": [],
                    "images": []
                }, f, ensure_ascii=False, indent=4)
            new_files_count += 1

print(f"✅ Đã tạo {new_files_count} file JSON mới cho page1 trong thư mục {label_dir}")