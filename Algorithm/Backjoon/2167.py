import sys
sys.stdin=open("input/2167.txt",'r')

# N,M = map(int, input().split())
# Matrix=[list(map(int, input().split())) for i in range(N)]
# K =int(input())
# for line in range(K):
#     i,j,x,y = map(int, input().split()) 
#     sum_=0                                
#     if j == y:
#         row_max=max(i,x)
#         column_max=max(j,y)
#     else:
#         row_max=N
#         column_max=max(j,y)
#     while 1:
#         sum_ += Matrix[i-1][j-1]
#         if i == x and j == y:
#             print(sum_)
#             break
#         elif i < row_max:
#             i += 1
#         else:
#             j +=1
#             i = 1


N, M = map(int, input().split())
matrix=[list(map(int, input().split())) for i in range(N)]

K = int(input())
sum_num = 0
# print(matrix)

for count in range(K):
    sum_num = 0

    i, j, x, y = map(int, input().split())

    for row in range(i-1, x):
        for line in range(j-1, y): # 행을 고정해놓고 열을 움직였음
            sum_num += matrix[row][line]
    print(sum_num)