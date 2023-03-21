import sys
sys.stdin=open("input/1236.txt",'r')

N,M=map(int, input().split())
Matrix=[list(input()) for i in range(N)]
cnt=0
N_row=[]
M_column=[]
for i in range(1,N+1):
    N_row.append(i)    
for i in range(1,M+1):
    M_column.append(i)  
for i in range(1,len(Matrix)+1):
    for j in range(1,len(Matrix[0])+1):
        if Matrix[i-1][j-1] =='X':
            if i in N_row:
                N_row.remove(i)
            elif i not in N_row:
                pass
            if j in M_column:
                M_column.remove(j)
            elif j not in M_column:
                pass
if N_row==[] and M_column==[]:
    print(0)
else:
    if len(N_row) > len(M_column):
        print(len(N_row))
    if len(N_row) < len(M_column):
        print(len(M_column))
    if len(N_row) == len(M_column):
        print(len(N_row))