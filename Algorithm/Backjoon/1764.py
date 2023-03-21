import sys

N,M=map(int,(input().split()))
dict={}
for i in range(N+M):
    word=sys.stdin.readline()  # 그냥 input보다 sys.stdin.readline()으로 받으니 4636 ms --> 140 ms로 줄어듦
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
keys=[]
for k,v in dict.items():
    if v >1:
        keys.append(k)
keys=sorted(keys)
print(len(keys))
for i in range(len(keys)):
    print(keys[i],end='')    

