a,b,c = map(int, input().split())
if a == b == c:
    print(10000+c*1000)
if (a==b and b !=c):
    print(1000+a*100)
if (a==c and c !=b):
    print(1000+a*100)
if (b==c and c !=a):
    print(1000+b*100)
if a !=b and a !=c and b!=c:
    print(max(a,b,c)*100)