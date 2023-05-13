import sys
sys.stdin = open('input/11387.txt','r')
# T = int(input())
# def demage(D, L, N):
#     demage = 0
#     for n in range(N):
#         demage += D*(1+n*L*(1/100))
#     return demage

# for i in range(T):
#     D,L,N = map(int,input().split())
#     result = demage(D,L,N)
#     print(f'#{i+1} {int(result)}')

T = int(input())
for i in range(T):
    D,L,N = map(int,input().split())
    demage=0
    for n in range(N):
        demage += D*(1+n*L(1/100))
    print(f'#{i+1} {int(demage)}')

