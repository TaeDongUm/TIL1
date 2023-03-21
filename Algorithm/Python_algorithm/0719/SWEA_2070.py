T = int(input())
for i in range(0,T):
    a,b = map(int, input().split())
    if a < b:
        print("#%d <" % (i+1))
    elif a == b:
        print("#%d =" % (i+1))
    elif a > b:
        print("#%d >" % (i+1))
