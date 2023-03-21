import sys
from pprint import pprint
sys.stdin=open("input/2606.txt")
# 인접 리스트로 풀려고 했지만 어려움
# dic={}
# Computer=int(input())
# Connected=int(input())
# Matrix=[[] for i in range(Computer+1)]
# for j in range(Connected):
#     a,b=map(int, input().split())
#     Matrix[a].append(b)
#     Matrix[b].append(a)
# print(Matrix)
# for k in range(len(Matrix[1])):
#     for m in range(len(Matrix[k])):
#         if Matrix[1][m] not in dic:
#             dic[Matrix[k][m]]=1
# key=dic.keys()
# print(len(key))

# len(Matrix[1])
# 인접 행렬로 풀어보려고 했음
dic={}
Computer = int(input())
Connected=int(input())
Matrix=[[0]*(Computer+1) for i in range(Computer+1)]
for i in range(Connected):
    a,b = map(int, input().split())
    Matrix[a][b]+=1
    Matrix[b][a]+=1
pprint(Matrix)
for i in range(Computer+1):
    if Matrix[i][1] ==1:  
        for k in range(1, Computer+1):
            if Matrix[i][k]==1:
                if k not in dic:
                    dic[k]=1
                else:
                    dic[k]+=1
key=dic.keys()
print(len(key)-1)