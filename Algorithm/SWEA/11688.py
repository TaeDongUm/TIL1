import sys
sys.stdin = open('input/11688.txt','r')
T = int(input())
for h in range(T):
    a=1
    b=1
    moving = input()
    for i in range(len(moving)):
        if moving[i] == 'L':
            b = a+b
        elif moving[i] == 'R':
            a = a+b
    print(f'#{h+1} {a} {b}')