X=int(input())
N=int(input())
sum_=0
for i in range(N):
    a, b = list(map(int, input().split()))
    sum_+= a*b
if sum_ == X:
    print("Yes")
else:
    print("No")