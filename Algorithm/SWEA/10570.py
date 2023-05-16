import sys
import math
from collections import deque
sys.stdin = open('input/10570.txt','r')

T = int(input())
for i in range(T):
    deque1=deque()
    a, b = map(int, input().split())
    count =0
    ForBreak= False
    list = []
    # 주어진 범위를 탐색
    for j in range(a,b+1):
        length_check=0
        deque1=deque(str(j))
        # 일의 자리만 살펴볼 때
        if len(str(j)) ==1:
            if (int(math.sqrt(int(j))))**2==int(j):
                count +=1
                continue
        # 두자리를 살펴볼 때
        while len(deque1)>1:
            x=deque1.pop()
            y=deque1.popleft()
            # 제곱 팰린드롬인지 확인
            if x ==y and (int(math.sqrt(int(j))))**2==int(j):
                k = int(math.sqrt(int(j)))
                deque2 = deque(str(k))
                v = deque2.pop()
                w = deque2.pop()
                if v == w:
                    length_check +=2
        # 두자리일 때 조건에 맞는 수 counting하기
        if len(str(j)) !=1 and len(str(j))%2==0 and len(str(j)) == length_check:
            count +=1
            list.append(j)
        elif len(str(j)) !=1 and len(str(j))%2 !=0 and len(str(j)) ==length_check+1:
            count +=1
            list.append(j)
    print(f'#{i+1} {count}')

# 팰린드롬, 제곱 팰린드롬 각각을 함수로 만드는 것이 좋을 듯
# 제곱 팰린드롬의 경우 제곱을 취하였을 때 그 수가 팰린드롬인지 파악을 안해서 틀림

# T = int(input())
 
# for test_case in range(1, T + 1):
#     a, b = map(int, input().split())
#     cnt =0
#     for i in range(a, b+1):
#         if list(str(i)) == list(str(i))[::-1]:
#             tmp = int(i ** (1/2))
#             if tmp * tmp == i and list(str(tmp)) == list(str(tmp))[::-1]:
#                 cnt += 1
#     print(f"#{test_case} {cnt}")

# T = int(input())
 
# for test_case in range(1, T + 1):
#     A, B = map(int, input().split())
#     answer = 0
  
#     for i in range(A, B+1):
#         C = i**(1/2)
#         if C == int(C):
#             if str(i) == str(i)[::-1] and str(int(C)) == str(int(C))[::-1]: 
#                 answer += 1
        
#     print(f"#{test_case} {answer}")

# import math
 
 
# def check_pal(s):
#     s = list(s)
#     length = len(s)//2
 
#     for i in range(length):
#         if s[i] != s[len(s)-i-1]:
#             return False
 
#     return True
 
 
# def sol(a, b):
#     ans = 0
 
#     for i in range(a, b+1):
#         comV1 = math.sqrt(i)
#         comV2 = int(math.sqrt(i))
#         if comV1 != comV2:
#             continue
#         if check_pal(str(i)) and check_pal(str(comV2)):
#             ans += 1
#     return ans
 
 
# for tc in range(int(input())):
#     a, b = map(int, input().split())
#     res = sol(a, b)
#     print(f'#{tc+1} {str(res)}')


