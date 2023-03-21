import sys
from pprint import pprint
sys.stdin = open("input/2669.txt",'r')
max_x=0
max_y=0
Matrix=[list(map(int, input().split())) for i in range(4)]
for i in range(4):
    if max_x <= max(Matrix[i][0],Matrix[i][2]):
        max_x=max(Matrix[i][0],Matrix[i][2])
    if max_y <= max(Matrix[i][1],Matrix[i][3]):
        max_y=max(Matrix[i][1],Matrix[i][3])
Graph=[[0]*(max_x+1) for i in range(max_y+1)]
for i in range(4):
    for k in range(Matrix[i][1]+1,Matrix[i][3]+1):
        for j in range(Matrix[i][0]+1,Matrix[i][2]+1):
            Graph[k][j] = True
cnt=0
for k in range(len(Graph)):
    for j in range(len(Graph[k])):
        if Graph[k][j]==1:
            cnt+=1
print(cnt)

# graph = [[0] * 101 for _ in range(101)]

# for _ in range(4):
#     x1, y1, x2, y2 = map(int,input().split())
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             graph[i][j] = 1
# area = 0
# for i in graph:           # !(나와의 차이점) 여기서 굳이 for문으로 돌릴 필요없다.
#     area += i.count(1)
# print(area)