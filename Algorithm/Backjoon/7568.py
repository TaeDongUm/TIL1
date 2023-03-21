import sys
sys.stdin = open("input/7568.txt",'r')

N=int(input())
people=[]
cnt=0
rank=[]
for i in range(N):
    body = list(map(int, input().split())) # clear 할 필요없이 새로운 값을 받음
    people.append(body)
for j in range(len(people)):
    for k in range(len(people)):
        if j ==k:
            continue
        if people[j][0] < people[k][0] and people[j][1] < people[k][1]:
            cnt+=1
    
    rank.append(cnt+1)
    cnt=0
print(*rank)
