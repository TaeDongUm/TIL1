T=int(input())
num1=[]
num2=[]
for i in range(0,T):
    a, b = map(int, input().split())
    num1.append(a // b)
    num2.append(a % b)
for i in range(0,T):
    print("#%d %d %d" % (i+1, num1[i], num2[i]))
