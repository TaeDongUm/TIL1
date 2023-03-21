# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
# 123
# 출력 6

num = int(input())
cnt = 0
sum =0
while 1:
        n = num % 10**(cnt+1)
        num = num - n
        n1 = n // 10**(cnt)
        sum = sum + n1
        cnt +=1
        if num == 0:
            print(sum)
            break