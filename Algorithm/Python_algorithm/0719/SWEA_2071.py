T = int(input())

for i in range(0,T):
    a = list(map(int, input().split()))
    sum =0
    for j in range(10):
        sum = sum + a[j]
    print("#%d " % (i+1), end='')
    print(round(sum/10))



# for i in range(0,T):
#     a = list(map(int, input().split()))
    
#     for j in range(10):
#         sum = sum + a[j]
#     print("#%d " % (i+1), end='')
#     print(round(sum/10))
#     sum =0
# 위 코드와 다르게 sum =0을 아래쪽에 두면
# Error Message: #Memory error occured,
# (e.g. segmentation error, memory limit Exceed, stack overflow,... etc) 이런 에러가 뜸
# 위쪽 코드에서 sum이라는 변수에 0을 초기화해서 사용해서 그렇다. 파이썬에는 sum()이라는 내장함수가 존재함
# 따라서, 위쪽 코드가 작동하기는 하지만, 내장함수와 같은 이름의 변수 사용은 지양하는게 좋다!
    
            
