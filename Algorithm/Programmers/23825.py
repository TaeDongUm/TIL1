N,M = map(int, input().split())
num = 0
if N<M:
    num =N
if N>M:
    num =M
if N == M:
    num =N
print(num // 2, end='')