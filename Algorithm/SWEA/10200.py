import sys
sys.stdin = open('input/10200.txt', 'r')
T= int(input())
for i in range(T):
    min_=0
    max_=0
    N, A, B = map(int,input().split())
    if A + B <=N:
        max_=min(A,B)
        print(f'#{i+1} {max_} {min_}')
    else:
        if N > max(A,B):
            max_=min(A,B)
            min_= abs(N - max(A,B) - min(A,B))
            print(f'#{i+1} {max_} {min_}')
        elif N == max(A,B):
            if min(A,B) == max(A,B):
                max_, min_ = max(A,B),max(A,B)
            else:
                max_=min(A,B)
                min_= N - max(A,B) + min(A,B)
            print(f'#{i+1} {max_} {min_}')

# T = int(input())
 
# for test_case in range(1, T + 1):
#     n, a, b = map(int, input().split())
#     max_num = min(a, b)
#     min_num = max(0, a - (n - b))
#     print("#" + str(test_case) + " " + str(max_num) + " " + str(min_num))
