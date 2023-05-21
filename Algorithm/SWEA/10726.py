import sys
sys.stdin = open('input/10726.txt','r')
T= int(input())
for i in range(T):
    N, M = map(int, input().split())
    binary=[]
    while M>0:
        binary.append(M%2)
        M =M//2
    for j in range(N):
        if len(binary)<N:
            break
        elif binary[j]==1:
            N-=1
        else:
            continue
    if N ==0:
        print('#{} ON'.format(i+1))
    else:
        print(f'#{i+1} OFF')