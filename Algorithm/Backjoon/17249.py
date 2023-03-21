punch=input()
cnt =0
num=[]
for i in range(len(punch)):
    if punch[i] == '@':
        cnt+=1
    if punch[i]==')':
        num.append(cnt)
        cnt=0
    if i == len(punch)-1:
        num.append(cnt)

print(*num)

