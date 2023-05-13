import sys
sys.stdin = open('input/11736.txt','r')
T = int(input())
for i in range(T):
    N = int(input())
    sequence = list(map(int,input().split()))
    count = 0
    for j in range(1,len(sequence)-1):
        if sequence[j-1] < sequence[j] and sequence[j] < sequence[j+1]:
            count +=1
        if sequence[j+1] < sequence[j] and sequence[j] < sequence[j-1]:
            count +=1
    print(f'#{i+1} {count}')

# T=int(input())
# for t in range(T):
#     N=int(input())
#     p=list(map(int, input().split()))
#     count=0
#     for i in range(1, N-1):
#         if p[i-1]<=p[i]<=p[i+1] or p[i+1]<=p[i]<=p[i-1]:
#             count+=1
#     print(f'#{t+1} {count}')
