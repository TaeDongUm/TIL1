N = int(input())
for i in range(N):
    if N % (i+1) == 0:
        divisor = i+1
        print("%d " % (divisor), end="")