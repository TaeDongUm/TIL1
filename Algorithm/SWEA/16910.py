T = int(input())
for i in range(T):
    count = 0   
    N = int(input())
    for x in range(1,N+1):
        # 1사분면
        for y in range(1,N+1):
            num = x**2 + y**2
            if (num <=N**2):
                count += 1
        # 4사분면
        for y in range(0, N+1):
            if (x**2 + (-y)**2 <=N**2):
                count += 1
    for x in range(0, N+1):
        # 2사분면
        for y in range(1,N+1):
            if ((-x)**2 + y**2) <=N**2:
                count += 1
        # 3사분면
        for y in range(0, N+1):
            if (-x)**2 + (-y)**2 <=N**2:
                count += 1
    print(f'#{i+1} {count}')