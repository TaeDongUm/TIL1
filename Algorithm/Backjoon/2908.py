a,b = map(int, input().split())
cnt =0

def changeValue(a):
    n2=0
    value = len(str(a))
    for i in range(value):
        n1 = a % 10
        a = a//10
        n2 += n1*(10**(value-1-i))
    return n2
if changeValue(a) >= changeValue(b):
    print(changeValue(a))
else:
    print(changeValue(b))

# import sys

# sys.stdin = open("1_상수.txt")

# a, b = input().split()      # 두 숫자를 a, b로 넣음

# a = int(a[::-1])
# b = int(b[::-1])            # 각 숫자를 거꾸로 한 뒤 int로 타입변경

# print(a if a > b else b)    # a > b면 a를, 아니면 b를 출력