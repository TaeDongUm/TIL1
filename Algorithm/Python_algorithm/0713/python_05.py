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

# 다른 풀이

numbers = [3, 10 ,20]

result =0
count =0

for number in numbers:
    result = result + number
    count = count + 1

    print(result/count)