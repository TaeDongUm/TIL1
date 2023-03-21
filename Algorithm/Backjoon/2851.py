#import sys
#sys.stdin=open('input/2851.txt')

num=[]
sum_=0
score=0
for i in range(10):
    num.append(int(input()))
for i in range(len(num)):
    sum_+=num[i]
    if sum_ >=100:
        if (100-sum_+num[i]) > abs(100-sum_):
            print(sum_)
            break
        elif (100-sum_+num[i]) < abs(100-sum_):
            print(sum_-num[i])
            break
        elif (100-sum_+num[i]) == abs(100-sum_):
            print(sum_)
            break
    elif i==9:
        print(sum_)
        break

num=[]
sum_=0
score=0
for i in range(10):
    num.append(int(input()))
for i in range(len(num)):
    sum_+=num[i]
    if sum_ >=100:
        if (100-sum_+num[i]) > abs(100-sum_):
            break
        elif (100-sum_+num[i]) < abs(100-sum_):
            sum_=sum_-num[i]
            break
        elif (100-sum_+num[i]) == abs(100-sum_):
            break
print(sum_)

