testcase = int(input())
for i in range(testcase):
    N, D = map(int, input().split())
    D = D*2 +1
    if N%D ==0:
        water = N//D
    else:
        water = (N // D) + 1
    print(f'#{i+1} {water}')