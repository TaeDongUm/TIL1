T = int(input())
cnt = 0 
for i in range(T):
    if T == 1:
        print('*', end='')
    else:
        while 1:
            if i < len(range(T))-1:
                print(' ', end='')
            cnt += 1
            if cnt>=(len(range(T))-1):
                break
        cnt = 0
        while 1:
            print('*', end='')
            cnt += 1
            if i<cnt:
                break
        print('')
        
        