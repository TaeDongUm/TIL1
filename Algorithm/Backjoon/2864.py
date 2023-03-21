n, m = map(int, input().split())
max_=max(n,m)
min_=min(n,m)
if '6' in str(max_):
    max_=str(max_).replace('6','5')
if '6' in str(min_):
    min_=str(min_).replace('6','5')
min_value = int(max_)+ int(min_)
print(min_value, end=' ')
if '5' in str(max_):
    max_=str(max_).replace('5','6')
if '5' in str(min_):
    min_=str(min_).replace('5','6')
max_value = int(max_)+ int(min_)
print(max_value)

# a, b = map(str, input().split())
# print(int(a.replace('6', '5')) + int(b.replace('6', '5')), int(a.replace('5', '6')) + int(b.replace('5', '6')))

# string으로 입력을 받으면 된다.
# A, B = map(str, input().split())
# A = A.replace('6', '5')
# B = B.replace('6', '5')
# print(int(A)+int(B), end=' ')        
# A = A.replace('5', '6')
# B = B.replace('5', '6')
# print(int(A)+int(B))  