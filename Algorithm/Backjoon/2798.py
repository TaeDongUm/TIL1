import sys
sys.stdin=open("input/2798.txt")

N,M=list(map(int, input().split()))
Card=list(map(int, input().split()))
min=M

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            score = Card[i] + Card[j] + Card[k]
            if score<=M:
                if min >= M-score:
                    min = M-score
print(M-min)

