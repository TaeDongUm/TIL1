# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# while 문
"""n = int(input())

sum=1
while(n!=0):
    sum = sum*n
    n=n-1
print(sum)"""
    
# for문

n = int(input())
sum=1
for i in range(1,n+1):
    sum = sum*i
print(sum)

