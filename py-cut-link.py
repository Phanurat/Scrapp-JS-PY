import re
import sys

def find_similar_links(search_string, file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
            links = re.findall(r'(https?://\S+)', file_content)
            similar_links = [link for link in links if search_string in link and '?comment_id=' not in link]
            return similar_links
    except FileNotFoundError:
        return ["File not found!"]

def save_cut_links(similar_links, output_file):
    try:
        with open(output_file, "w") as file:
            for link in similar_links:
                file.write(link + "\n")  # Write the actual link to the file
        print("Cut links saved successfully!")
        sys.exit()  # ปิดโปรแกรมหลังจากบันทึกไฟล์เสร็จ
    except FileNotFoundError:
        print("Output file directory not found.")

def get_and_save_links():
    with open("url_page/url_page.txt", "r", encoding="utf-8") as url_file:
        search_string = url_file.read().strip()  # อ่าน URL จากไฟล์ url_page.txt
        search_string += "/posts/"  # เพิ่มสตริง "/posts/" ต่อท้าย URL
    similar_links = find_similar_links(search_string, "get_link/output.txt")
    if similar_links:
        print("Link ถูก Cut เรียบร้อยแล้ว")
        for link in similar_links:
            print(link)
        save_cut_links(similar_links, "link_cut/link.txt")
    else:
        print("No similar links found.")

# เรียกใช้ฟังก์ชัน get_and_save_links เพื่อเริ่มการทำงาน 
get_and_save_links()
