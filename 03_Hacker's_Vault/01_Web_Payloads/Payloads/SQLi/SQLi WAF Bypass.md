
[[Methodology - SQLi#📍 Phase 4 방화벽(WAF) 조우 시 비상 프로토콜]]


1. USE \
   
2. USE particular symbol
   0x0b, 0x0c.. etc
> 	/?id=1%0bor%0c1=1#
   > 	is equal
	   /?id=1 or 1=1#

3. USE &&, ||
   
4. USE like, in, <, >

5. substr(): substring(), mid(), left(), right(), lpad()
   ascii(): ord(), hex()
   sleep(): benchmark()