T = int(input())
cnt=0
for j in range(T):
    while 1:
        if j >= cnt:
            print('*',end='')
            cnt += 1
        else:
            break
    cnt = 0
    if j< len(range(T))-1:
        print('')
        