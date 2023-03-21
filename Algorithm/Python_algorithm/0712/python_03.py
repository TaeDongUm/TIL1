# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# while 문
"""n = int(input())
t=0
while(n!=0):
    t+=n
    n = n-1
print(t)"""

# for 문
n = int(input())
num =0
for i in range(1,n+1):
    num +=i
print(num)
