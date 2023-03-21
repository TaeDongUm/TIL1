import sys
input=sys.stdin.readline # 이걸 넣고 안넣고의 시간 차이가 크다
T=int(input())
for i in range(T):
    Price=0
    S= int(input())
    n = int(input())
    for j in range(n):
        q, p = list(map(int, input().split()))
        # q, p = map(int, input().split())
        Price += q*p
    print(Price + S)