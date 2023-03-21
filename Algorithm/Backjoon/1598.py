num1, num2=map(int, input().split())

row1 = num1 %4
if row1 ==0:
    row1 +=4
column1 = num1 //4
if num1 %4 ==0:
    column1-=1

row2 = num2 %4
if row2 ==0:
    row2 +=4
column2 = num2 //4
if num2 %4 ==0:
    column2-=1

index1=abs(row1-row2)
index2=abs(column1-column2)
print(index1+index2)
# 다른 사람 짧은 코딩 
# a, b = map(int,input().split())

# a -= 1
# b -= 1

# w = abs(a//4 - b//4)
# h = abs(a % 4 - b % 4)
# print(w+h)