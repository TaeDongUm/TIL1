import sys
sys.stdin=open('input/14361.txt','r')
T = int(input())

for i in range(T):
    n = int(input())
    m = list(str(n))
    count =0
    for j in range(2,10):
        k=0
        if len(str(n*j)) != len(str(n)):
            break
        else:
            k = list(str(n*j))
            if sorted(m) ==sorted(k):
                count +=1
            else:
                continue
    if count >=1:
        print('#{} possible'.format(i+1))
    else:
        print('#{} impossible'.format(i+1))
