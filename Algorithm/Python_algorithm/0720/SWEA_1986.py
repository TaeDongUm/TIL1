T = int(input())
N=[]
cnt =0
for i in range(T):
    N.append(int(input()))
for i in N:
    num = 0
    cnt += 1
    for j in range(i):
        n1 = 0
        n2 = 0
        if (j+1) % 2 == 0:
            n1 = -(j+1)
        elif (j+1) % 2 != 0:
            n2 = + (j+1)
        num = num + n1 + n2
    print(f'#{cnt} {num}')
    

