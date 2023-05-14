import sys
sys.stdin = open('input/11315.txt','r')

T = int(input())
dx=[0,1,1,1]
dy=[1,0,1,-1]
for i in range(T):
    N= int(input())
    graph=[]
    ForBreak = False
    # 입력으로 현재 오목판 받기
    for j in range(N):
        o_mok=input()
        graph.append(o_mok)
    # graph 인덱스에 접근해서 하나하나씩 살펴보기
    # row 이동
    for j in range(N):
        if ForBreak == True:
            break
        # column 이동
        for k in range(N):
            if ForBreak == True:
                break
            # 살펴볼 방향 선택
            for l in range(4):
                count =0
                # 해당 방향으로 5개 오목이 있는지 파악
                for m in range(5):
                    if 0<=j+dx[l]*m<=N-1 and 0<=k+dy[l]*m<=N-1 and graph[j+dx[l]*m][k+dy[l]*m] =='o':
                        count +=1
                    else:
                        break
                # 이게 문제인 것 같음
                if count != 5:
                    # break문을 넣으면 for l in range(4)를 벗어나서 다음 방향 선택이 안됨.
                    continue
                elif count == 5:
                    print(f'#{i+1} YES')
                    ForBreak = True
                    break
        if ForBreak == True:
            break
        elif j==N-1 and k == N-1:
            print(f'#{i+1} NO')
            break
    
# for else문: for문이 다 돌았을 때 else문 실행    
# def solve():
#     for si in range(n):
#         for sj in range(n):
#             for di,dj in ((0,1),(1,0),(1,1),(-1,1)):
#                 for mul in range(5):
#                     ni,nj = si+di*mul, sj+dj*mul
#                     if 0<=ni<n and 0<=nj<n and a[ni][nj] == 'o':
#                         pass
#                     else:
#                         break
#                 else:
#                     return 'YES'
#     return 'NO'
 
# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     a = [input() for _ in range(n)]
     
#     ans = solve()
     
#     print(f"#{tc} {ans}")
        