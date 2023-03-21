# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

n =1
number =2
while number <=9:
    while n<=9:
        if n ==1:
            print(f'{number}단')
        result = number*n
        print(f'{number} X {n}= {result}')
        n += 1
    n=1    
    number += 1