# 다른 파일 호출하기
# import sys
# sys.stdin=open('input/1100.txt','r')


# SWEA 15758
# # 최소공배수 구해서 문자열 비교하기 
# # x를 무조건 큰 값으로 정하기
# 참고사이트 https://sinawi.tistory.com/232
# x = 4
# y = 2
# if x < y:
#     x, y = y, x
# while y > 0:
#     x, y = y, x % y

# 문자열과 배열 지우기
# 문자열은 replace
# 배열은 remove

# deque 사용
# 동서남북 탐색

# list.sort() list의  원본 배열을 정렬, 반환된 값 없음
# sorted(list)  원본은 그대로, 반환된 값이 정렬된 값

# lstrip(), rstrip(), strip() 각각 왼쪽, 오른쪽, 양쪽 공백 제거
# 인자가 들어가면 각각 왼쪽에서부터, 오른쪽에서부터, 양쪽에서부터 인자 제거

# deque2=deque(input())
# print(deque2)
# list = ''.join(deque2)
# print(list)

# from collections import deque
# deque1=deque()
# deque1=[1,2,3,4]
# if deque1.pop() ==4: # 조건문을 실행해도 deque1에서 인자 빠져나감
#     print(deque1)

# deque1.pop()을 조건문에 넣게 되면 조건문이 실행될 때마다 pop이 일어남
# 즉, 맨 마지막 elif문이 실행된다면, while문 한 싸이클에 총 4번의 pop이 일어남
# 그래서 while문 한 싸이클에 한번의 pop이 일어나게 하려면
# pop한 값을 변수에 넣어주고 그 변수를 조건문에 넣는 것이 좋다.
# deque1=deque(input())
# list = []
# while len(deque1)>=1:
#     if   deque1.pop() =='b':
#         list.append('d')
#     elif deque1.pop() =='d':
#         list.append('b')
#     elif deque1.pop() =='p':
#         list.append('q')
#     elif deque1.pop() =='q':
#         list.append('p')

# binary=[1,1,0,1,0,1]
# while M>0:
#     binary.append(M%2)
#     M =M//2
# binary.reverse()
# print(binary)
x=[]
y=[]
for i in range(4,1):
    y.append(i)
    x.append(i)