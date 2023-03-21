ascending=[1,2,3,4,5,6,7,8]
descending=[8,7,6,5,4,3,2,1]
input_=list(map(int, (input().split())))
if input_ == ascending:
    print('ascending')
elif input_ == descending:
    print('descending')
else:
    print('mixed')

# n = list(map(int, input().split()))

# if n == sorted(n):
#     print('ascending')
# elif n == sorted(n, reverse=True):
#     print('descending')
# else:
#     print('mixed')