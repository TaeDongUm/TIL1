T = int(input())
money_A = 0
money_B = 0
for i in range(T):
    P,Q,R,S,W = map(int,input().split())
#A사
    money_A = P*W
#B사
    if W <= R:
        money_B = Q
    else:
        money_B = Q + S*(W-R)
#compare
    if money_A > money_B:
        print(f'#{i+1} {money_B}')
    else:
        print(f'#{i+1} {money_A}')