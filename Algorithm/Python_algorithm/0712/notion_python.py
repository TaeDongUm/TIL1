# 01.주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
''' n = int(input())
if(n%3 ==0) and (n%2 ==0):
    print('참')
else:
    print('거짓') '''

# 02. 문자열 word의 길이를 출력하는 코드를 각각 작성하시요. len() 함수를 쓰기보다는 반복문을 활용하세요.

"""word = input()
num =0
for i in word:
    num += 1
    word = word[1:]

print(num)

# 다른 풀이 참고

word = "happy!"

t = 0
while(word!=""):
    t+=1
    word = word[1:]
print(t)
"""

# 03. 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
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


# 04. 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
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

# 05. 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지
# numbers = [3, 10, 20]

num = list(map(int, input().split()))
sum =0
n=0
for i in num:
    sum += i
    n= n+1
sum = sum/n
print(sum)
