T = int(input())
cnt=0
for i in range(T):
    if T==1:
        print('*')
    else:

        if (i+1) % 2 ==0:
            print(' ', end='')
        while 1:
            print('*',end='')
            if cnt < len(range(T)):
                print(' ',end='')
            cnt += 1
            if cnt >= len(range(T)):
                break
        cnt =0
        if i < len(range(T))-1:
            print('')
        