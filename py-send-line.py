import requests

def get_access_token(file_path):
    try:
        with open(file_path, 'r') as file:
            access_token = file.read().strip()
            return access_token
    except FileNotFoundError:
        print("Token file not found.")
        return None

def send_message_via_line_notify(token_file, file_path):
    access_token = get_access_token(token_file)
    if not access_token:
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read().strip()
    except FileNotFoundError:
        print("File not found.")
        return
    
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {access_token}'}
    
    data = {'message': file_content}
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send message. Status code:', response.status_code)

# ไฟล์ที่เก็บ token
token_file = 'line_token/token.txt'

# ไฟล์ที่เก็บเนื้อหาที่ต้องการส่ง
file_path = './output/output_post.txt'

# ส่งข้อความผ่าน Line Notify API
send_message_via_line_notify(token_file, file_path)
