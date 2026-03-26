
[[Methodology - XSS#Phase 4 방화벽(WAF) 조우 시 비상 프로토콜]]

### replace string
   `scrSCRIPTipt`
   
### URL normalization
   브라우저에서 url을 사용하기 전에 문자열의 특수문자(`\`, `\t` 등)를 제거함
   
### \x(hex), \u(unicode)
   서버는 디코딩 로직이 없는 한 해독하지 않지만 브라우저의 JS엔진은 이를 해독한다.
   
   🚨 **주의: js용 암호임**
   - **❌ HTML 본문 (실패):** `< \u0073cript >` 브라우저의 'HTML 파서'는 `\u`가 뭔지 모른다. 그냥 텍스트로 취급해서 화면에 이상한 글자를 렌더링하고 끝난다. (이럴 땐 아까 배운 `&#x...;` HTML 엔티티를 써야 한다.)
   - **⭕ JS 문자열 내부 (성공):** `<script> var a = "\x61lert"; </script>` 자바스크립트가 돌아가는 구역 안이므로 완벽하게 해석된다.
   - **⭕ HTML 이벤트 핸들러 (성공):** `<img src=x onerror=\u0061lert(1)>` `onerror=""` 속성 안쪽은 자바스크립트가 실행되는 JS 영토다! 따라서 여기서 `\u`를 쓰면 마법처럼 `alert`로 변신한다.

### Special char filtering

1. dot
	`location.href` == `location['href']`
	`document.cookie` == `document['cookie']`
	
2. parentheses
   `alert(1)` == alert\`1\`
   
3. quote filtering
   alert.toString()\[14\]: '('
   
   32,36 진수로 변환
   parseInt("내용",진법)로 변환한걸로
   (내용).toString(진법)

### etc.

`<iframe>`
