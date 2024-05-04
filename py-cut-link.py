import tkinter as tk
from tkinter import messagebox
import re
import sys

def find_similar_links(search_string, file_path):
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            links = re.findall(r'(https?://\S+)', file_content)
            # เพิ่มเงื่อนไขในการค้นหาลิงก์
            similar_links = [link for link in links if search_string in link and '?comment_id=' not in link]
            return similar_links
    except FileNotFoundError:
        return ["File not found!"]

def save_cut_links(similar_links, output_file):
    try:
        with open(output_file, "w") as file:
            for link in similar_links:
                file.write(link + "\n")  # Write the actual link to the file
        messagebox.showinfo("Success", "Cut links saved successfully!")
        sys.exit()  # ปิดโปรแกรมหลังจากบันทึกไฟล์เสร็จ
    except FileNotFoundError:
        print("Output file directory not found.")

def get_and_save_links():
    search_string = entry.get()
    similar_links = find_similar_links(search_string, "get_link/output.txt")
    if similar_links:
        messagebox.showinfo("Success", "Link ถูก Cut เรียบร้อยแล้ว")
        for link in similar_links:
            print(link)
        save_cut_links(similar_links, "link_cut/link.txt")
    else:
        messagebox.showinfo("Error", "No similar links found.")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Cut Links")

# สร้าง Label แสดงข้อความ
label = tk.Label(root, text="Enter the search string:", padx=20, pady=10)
label.pack()

# สร้างช่อง input สำหรับรับค่า search string
entry = tk.Entry(root)
entry.pack()

# สร้างปุ่มเพื่อค้นหาลิงก์ที่คล้ายกันและบันทึกลิงก์ที่ตัดแล้ว
button_cut_links = tk.Button(root, text="Cut Links", command=get_and_save_links)
button_cut_links.pack()

# เริ่มการทำงานของ GUI
root.mainloop()
