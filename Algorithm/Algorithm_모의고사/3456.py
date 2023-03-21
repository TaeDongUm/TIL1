T = int(input())
for i in range(T):
    a,b,c = map(int,input().split())
    if a==b:
        print(f'#{i+1} {c}')
    if a!=b:
        if a==c:
            print(f'#{i+1} {b}')
        if b==c:
            print(f'#{i+1} {a}')