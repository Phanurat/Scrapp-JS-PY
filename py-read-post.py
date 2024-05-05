from bs4 import BeautifulSoup

# เปิดไฟล์ HTML
with open('html_post/content1_post.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# สร้างอ็อบเจ็กต์ BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# ค้นหา tag <meta> ที่มี attribute name="description"
description_meta_tag = soup.find('meta', attrs={'name': 'description'})

# ค้นหา tag <link> ที่มี attribute rel="canonical"
canonical_link_tag = soup.find('link', rel='canonical')

# ค้นหา tag <content>
title_tag = soup.find('title')

# เขียนข้อมูลลงในไฟล์ output.txt
with open('output/output_post.txt', 'w', encoding='utf-8') as f:

    # ตรวจสอบว่ามี tag <title> หรือไม่
    if title_tag:
        title_text = title_tag.text.strip()
        f.write("Title: " + title_text + "\n\n")
    else:
        f.write("No <title> tag found in the HTML.")

    # ตรวจสอบว่ามี tag <meta> ที่มี attribute name="description" หรือไม่
    if description_meta_tag:
        description_content = description_meta_tag['content']
        f.write("Description: " + description_content + "\n\n")
    else:
        f.write("No <meta name='description'> tag found in the HTML.\n\n")

    # ตรวจสอบว่ามี tag <link> ที่มี attribute rel="canonical" หรือไม่
    if canonical_link_tag:
        canonical_link = canonical_link_tag['href']
        f.write("Canonical Link: " + canonical_link + "\n\n")
    else:
        f.write("No <link rel='canonical'> tag found in the HTML.\n\n")

    
