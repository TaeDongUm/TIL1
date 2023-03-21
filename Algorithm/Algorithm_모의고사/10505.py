T = int(input())
for i in range(T):
    sum_=0
    Average=0
    cnt=0
    N = int(input())
    Salary=list(map(int,input().split()))
    for j in Salary:
        sum_ += j
        Average = sum_/N
    for k in Salary:
        if Average >= k:
            cnt +=1
    print(f'#{i+1} {cnt}')
