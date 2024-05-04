import json

# กำหนดที่อยู่ของไฟล์ที่มีลิงก์ link.txt
file_path = "link_cut/link.txt"

# อ่านข้อมูลจากไฟล์ link.txt
with open(file_path, "r") as link_file:
    # อ่านและแยกลิงก์ตามบรรทัด
    links = link_file.readlines()

# สร้าง dictionary ที่จะเก็บข้อมูลลิงก์
links_dict = {}

# วนลูปเพื่อสร้างโครงสร้างข้อมูล JSON
for i, link in enumerate(links, start=1):
    link_key = f"Link{i}"
    link_value = {"link": link.strip()}
    links_dict[link_key] = link_value

# สร้างโครงสร้างข้อมูล JSON ที่มีรายการของลิงก์
data = {"links": links_dict}

# กำหนดที่อยู่ของไฟล์ JSON ที่ต้องการจะเขียน
json_file_path = "json_news/links.json"

# เขียนข้อมูลลงในไฟล์ JSON
with open(json_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("เก็บลิงก์เป็น JSON สำเร็จแล้ว!")
