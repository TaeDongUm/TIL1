import sys
sys.stdin=open('15612.txt','r')

Testcase = int(input())
for i in range(Testcase):
    graph = []
    for _ in range(8):
        graph.append(list(input()))
    count = 0
    ForBreak = False
    # 서남동북 순으로 찾기
    for k in range(len(graph)):
        for j in range(len(graph[k])):
            if graph[k][j] == 'O':
                count += 1
                moving = 1
                # 서쪽 살펴보기
                while j-moving>=0:
                    if graph[k][j-moving] == 'O':
                        ForBreak = True
                        break
                    moving += 1
                # 남쪽 살펴보기
                if ForBreak == True:
                    break
                moving  = 1
                while k+moving<=7:
                    if graph[k+moving][j] == 'O':
                        ForBreak = True
                        break
                    moving += 1
                # 동쪽 살펴보기
                if ForBreak == True:
                    break
                moving = 1
                while j+moving<=7:
                    if graph[k][j+moving] == 'O':
                        ForBreak = True
                        break
                    moving += 1
                # 북쪽 살펴보기
                if ForBreak == True:
                    break
                moving = 1
                while k-moving>=0:
                    if graph[k-moving][j] == 'O':
                        ForBreak = True
                        break
                    moving += 1
                if ForBreak == True:
                    break
            if ForBreak == True:
                break
        if ForBreak == True:
            break
    # 탐색 다 끝나고 나서 룩이 8개 이상이면
    if ForBreak == True:
        print(f'#{i+1} no')
        continue
    elif count > 8 or count < 8:
        print(f'#{i+1} no')
        continue
    elif count == 8:
        print(f'#{i+1} yes')
        continue

# 
# tc = int(input())
 
# for t in range(tc):
#     isVisted = [False] * 8
#     check = list(input() for _ in range(8))
#     for i in check:
#         if i.count('O') != 1:
#             break
 
#         if isVisted[i.index('O')] == False:
#             isVisted[i.index('O')] = True
#         else:
#             break
 
#     if False in isVisted:
#         print(f"#{t+1} no")
#     else:
#         print(f"#{t+1} yes")

# T = int(input())
# for test_case in range(1, T + 1):
#     graph = [list(input()) for _ in range(8)]
#     z = list(zip(*graph))
#     flag = False
#     for idx in range(8):
#         if graph[idx].count('O') != 1 or z[idx].count('O') != 1:
#             flag = True
#     if flag:
#         print("#%d no" % test_case)
#     else:
#         print("#%d yes" % test_case)
    