import math
testcase = int(input())
for i in range(testcase):
    TC = int(input())
    goal_index = []
    for x in range(1, int(math.sqrt(TC))+1): # 제곱근으로 최대한 계산을 줄임
        if TC % x ==0:
            goal_index.append([x,(TC//x)])
    x = 1
    y = 1
    count = []
    for index in goal_index:
        distance = 0
        distance += index[0] - x
        distance += index[1] - y
        count.append(distance)
    print(f'#{i+1} {min(count)}')
# seconds =0.19169s

# import math
# T = int(input())
# for test_case in range(1, T + 1):
#     n = int(input())
#     arr = []
#     for i in range(1, int(math.sqrt(n))+1):
#         if n % i == 0:	#곱해서 n이 되는 두 수 찾기
#             arr.append((i, n//i))
#     for i, (x, y) in enumerate(arr):	#index, (x, y)
#         arr[i] = (x-1)+(y-1)	#배열의 각 인덱스에 (1, 1)->(x, y)까지 이동거리 저장
#     print("#{} {}".format(test_case, min(arr)))
# seconds = 0.15207s