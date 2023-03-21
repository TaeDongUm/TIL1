import sys
from pprint import pprint
sys.stdin=open("input/2897.txt")
R, C = map(int, input().split())
Matrix=[]
for i in range(R):
    Matrix.append(list(input()))
dx=[0,0,1,1]
dy=[0,1,0,1]
Parking=[0,0,0,0,0]
X_Count=0
ForBreak=True
for j in range(R-1):
    for k in range(C-1):
        for m in range(4):
            if Matrix[j+dx[m]][k+dy[m]] =='#':
                ForBreak=False
                X_Count=0
                break
            elif Matrix[j+dx[m]][k+dy[m]] =='X':
                X_Count+=1
        if ForBreak==False:
            ForBreak=True
            continue
        if X_Count==0:
            Parking[0]+=1
        if X_Count==1:
            Parking[1]+=1
        if X_Count==2:
            Parking[2]+=1
        if X_Count==3:
            Parking[3]+=1
        if X_Count==4:
            Parking[4]+=1
        X_Count=0
for i in range(len(Parking)):
    print(Parking[i])

# R, C = map(int, input().split())
# parking = [list(input()) for _ in range(R)]
# delta = ((0, 0), (1, 0), (0, 1), (1, 1))
# truck = []
# crush = [0, 0, 0, 0, 0]

# for r in range(R-1) :
#     for c in range(C-1) :
#         for dr, dc in delta :
#             truck.append(parking[r+dr][c+dc])
#         if truck.count('#') == 0 :
#             crush[truck.count('X')] += 1
#         truck.clear()

# print(*crush, sep='\n')
# 내 코드 또한 72ms로 짧지만 코드 길이가 짧아서 공부할 필요 있다.


