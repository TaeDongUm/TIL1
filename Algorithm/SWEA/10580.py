import sys
sys.stdin = open('input/10580.txt','r')

T = int(input())
for i in range(T):
    N = int(input())
    count =0
    check=[]
    for j in range(N):
        a,b =map(int,input().split())
        if check:
            for k in range(len(check)):
                if (a>check[k][0] and b <check[k][1]) or (a<check[k][0] and b>check[k][1]):
                    count +=1
        check.append((a,b))
    print(f'#{i+1} {count}')