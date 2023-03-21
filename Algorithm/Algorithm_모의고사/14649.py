import sys
sys.stdin=open("예제입력.txt",'r')
T = int(input())
for i in range(T):
    num=list(map(int, input().split()))
    sum_even=0
    sum_odd=0
    for j in range(1,len(num)+1):
        if j %2 ==0:
            sum_even += num[j-1]
        else:
            sum_odd += 2*num[j-1]
    for k in range(10):
        if (sum_even + sum_odd + k) %10 ==0:
            print(f'#{i+1} {k}')

