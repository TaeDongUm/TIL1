import sys
T=int(sys.stdin.readline())
dict={}
for i in range(T):
    number=int(sys.stdin.readline())
    if number not in dict:
        dict[number]=1
    else:
        dict[number]+=1
max_=max(dict.values())
keys=[]
for k,v in dict.items():
    if v==max_:
        keys.append(k)
keys=sorted(keys)
print(keys[0])
    