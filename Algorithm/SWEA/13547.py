T = int(input())
for i in range(T):
    winlose=input()
    count = winlose.count('x')
    if count >=8:
        print("#{} NO".format(i+1))
    else:
        print("#{} YES".format(i+1))