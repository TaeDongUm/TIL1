a,b = map(int, input().split())
num = 0
if a<b:
    num =a
if a>b:
    num =b
if a == b:
    num =a
print(num // 2)