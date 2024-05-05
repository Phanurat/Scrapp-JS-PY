import tkinter as tk
from tkinter import messagebox
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

# Create the main window
root = tk.Tk()
root.title("Cut Links")

# Create a label to display the message
label = tk.Label(root, text="Enter the search string:", padx=200, pady=10)
label.pack()

# Create an input entry for the search string
entry = tk.Entry(root)
entry.pack()

# Create a button to find similar links and save cut links
button_cut_links = tk.Button(root, text="Cut Links", command=get_and_save_links)
button_cut_links.pack()

# Start the GUI operation
root.mainloop()
