num=[]
sum_=0
for i in range(5):
    n1=int(input())
    num.append(n1)
    sum_+=n1
print(round(sum(num)/5))
num=sorted(num)
print(sorted(num))
print(num[2])

