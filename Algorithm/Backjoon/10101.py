a=int(input())
b=int(input())
c=int(input())

# if a==60 and b ==60 and c==60:
#     print('Equilateral')
# if a+b+c==180 and ((a==b and c!=a) or (a==c and b!=a)):
#     print("Isosceles")
# if a+b+c==180 and (a!=b!=c): # 이렇게 하면 틀림 
#     print("Scalene")
# if a+b+c!=180:
#     print("Error")

#     a=int(input())
# b=int(input())
# c=int(input())

if a==60 and b ==60 and c==60:
    print('Equilateral')
if a+b+c==180 and ((a==b and c!=a) or (a==c and b!=a) or (b==c and b!=a)):
    print("Isosceles")
if a+b+c==180 and (a!=b and b!=c and a!=c):
    print("Scalene")
if a+b+c!=180:
    print("Error")