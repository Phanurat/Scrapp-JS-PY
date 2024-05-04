from bs4 import BeautifulSoup
from pythainlp.tokenize import word_tokenize

word_cut = ['test']

# เปิดไฟล์ HTML
with open('scrap/test_cut.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# สร้างอ็อบเจ็กต์ BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# เก็บข้อความที่พิมพ์ออกมาไว้ในเซ็ตเพื่อตรวจสอบ
printed_text = set()

# เปิดไฟล์ output.txt ในโหมดการเขียน ('w') เพื่อเตรียมเขียนข้อมูล
with open('output/output_post.txt', 'w', encoding='utf-8') as f:
    # ค้นหาและตัดคำในแท็ก <span>
    for paragraph in soup.find_all('span'):
        # ตรวจสอบว่าข้อความภายในแต่ละ <span> ไม่ซ้ำกับข้อความที่มีอยู่แล้ว และไม่ซ้ำกับ word_cut
        if paragraph.get_text() not in word_cut and paragraph.get_text() not in printed_text:
            words = word_tokenize(paragraph.get_text(), engine='newmm')  # แบ่งคำ
            words_filtered = [word for word in words if word not in word_cut]  # เลือกเฉพาะคำที่ไม่อยู่ใน word_cut
            output_line = ''.join(words_filtered)  # รวมคำที่ถูกตัดออกมาแล้วรวมกันในรูปแบบของข้อความ
            print(output_line)  # พิมพ์รายการคำที่ถูกตัดออกมาแล้วรวมกัน
            f.write(output_line + '\n')  # เขียนข้อมูลลงในไฟล์ output.txt
            printed_text.add(paragraph.get_text())  # เพิ่มข้อความลงในเซ็ตเพื่อที่จะไม่พิมพ์อีกครั้ง