import sys
sys.stdin=open("input/5533.txt","r")

N=int(input())
Matrix=[list(map(int,input().split())) for i in range(N)]
score=[0]*N
index_check=[]
for Gamenum in range(3):  # 게임 번호
    for i in range(N-1):    #  
        for j in range(1+i,N): 
            if Matrix[i][Gamenum] == Matrix[j][Gamenum]:
                index_check.append(i)
                index_check.append(j)
    for k in range(N):
        if k not in index_check:
            score[k]+=Matrix[k][Gamenum]
    index_check=[]   
for l in range(len(score)):
    print(score[l])     
        








# New_Matrix=[]
# list=[]
# for i in range(3):
#     for j in range(5):
#         list.append(Matrix[j][i])
#     New_Matrix.append(list)
#     list=[]    
# print(New_Matrix)
    