# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

num = int(input())
num1=num
cnt = 0
while 1:
        n = num % 10**(cnt+1)
        cnt +=1
        num = num - n
        if num == 0:
            print(cnt)
            break
sum = 0
cnt1 = 0
while 1:
        n = num1 % 10**(cnt1+1)
        num1 = num1 - n
        n1 = n // 10**(cnt1)
        sum = sum + n1*(10**(cnt-1))
        cnt -= 1
        cnt1 += 1
        if cnt == 0:
            print(sum)
            break