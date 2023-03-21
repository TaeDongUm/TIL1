num=[]
sum_=0
cnt=1
for i in range(1,51):
    for j in range(i,i+cnt):
        num.append(i)
    cnt +=1
A, B = map(int, input().split())
for i in range(B-A+1):
    sum_ += num[A-1+i]
print(sum_)
 