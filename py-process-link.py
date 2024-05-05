import json
import os

# อ่านข้อมูลจากไฟล์ link.txt
file_path = "link_cut/link.txt"
with open(file_path, "r") as link_file:
    links = link_file.readlines()

# สร้างโฟลเดอร์ link_post ถ้ายังไม่มี
if not os.path.exists("link_post"):
    os.makedirs("link_post")

# สร้างไฟล์ในโฟลเดอร์ link_post สำหรับแต่ละ link
for i, link in enumerate(links, start=1):
    link = link.strip()
    file_name = f"link_post/link{i}.txt"
    with open(file_name, "w") as output_file:
        output_file.write(link)

    print(f"ไฟล์ {file_name} ถูกสร้างเรียบร้อยแล้ว")
