T = int(input())
for i in range(T):
    a,b =map(int, input().split())
    if a>=10 or b>=10:
        print(f'#{i+1} -1')
    else:
        print(f'#{i+1} {a*b}')
