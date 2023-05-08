testcase = int(input())
for i in range(testcase):
    N = int(input())
    y=2
    x = y + N
    X = 0
    Y = 0
    while 1:
        if x-y == N:
            # 합성수인지 아닌지 판단
            for a in range(2, x):
                if x % a == 0:
                    X = x
                    break
            for a in range(2,y):
                if y % a == 0:
                    Y = y
                    break
            if X != 0 and Y != 0:
                print(f'#{i+1} {X} {Y}')
                break
            else:
                X = 0
                Y = 0
                x += 1
                y += 1
