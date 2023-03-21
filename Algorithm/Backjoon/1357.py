X, Y = map(int, input().split())
def Rev(num):
    new_num=0
    num1 =num
    for i in range(len(str(num1))):
        n1 = num % 10
        new_num += n1*(10**(len(str(num1))-(i+1)))
        num //= 10
        if num ==0:
            return new_num
print(Rev(Rev(X)+ Rev(Y)), end='')

