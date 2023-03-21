a,b =map(int,input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=A+B
dic={}
for i in C:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
C=[]
for k,v in dic.items():
    if v <2:
        C.append(k)
print(len(C))
