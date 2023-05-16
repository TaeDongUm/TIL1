import sys
sys.stdin = open('input/10505.txt','r')
T = int(input())

for i in range(T):
    N = int(input())
    income = list(map(int,input().split()))
    sum_ =0
    count =0
    for j in range(len(income)):
        sum_ += income[j]
    mid = sum_/(len(income))
    for j in range(len(income)):
        if mid >= income[j]:
            count +=1
    print(f'#{i+1} {count}')

