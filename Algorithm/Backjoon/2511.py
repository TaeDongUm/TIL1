import sys
sys.stdin=open("input/2511.txt")
# Card_numA=list(map(int,input().split()))
# Card_numB=list[map(int, input().split())]
# print(Card_numA)
# print(Card_numB)
# [4, 5, 6, 7, 0, 1, 2, 3, 9, 8]
# list[<map object at 0x000001EE856313D0>]  ---> 중괄호랑 대괄호의 차이
Score=[]
Card_numA=list(map(int,input().split()))
Card_numB=list(map(int,input().split()))
score_A=0
score_B=0
for i in range(10):
    if Card_numA[i] > Card_numB[i]:
        Score.append("A")
    if Card_numA[i] < Card_numB[i]:
        Score.append("B")
    if Card_numA[i] == Card_numB[i]:
        Score.append("D")
for i in Score:
    if i =='A':
        score_A +=3
    elif i =='B':
        score_B +=3
    elif i =='D':
        score_A +=1
        score_B +=1
print(score_A, score_B, sep = ' ')
if score_A > score_B:
    print("A")
elif score_A < score_B:
    print("B")
elif score_A == score_B:
    # Score(reversed, True) 이렇게 적으면 틀림
    Score.reverse()
    for i in Score:
        if i == 'A':
            print("A")
            break
        elif i =="B":
            print("B")
            break
    if 'A'and 'B' not in Score:
        print("D")

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# if A == B:
#     print(10, 10); 
#     print("D")
# else:
#     a = b = 0
#     for i in range(10):
#         if A[i] > B[i]:
#             a += 3; win = 'A'
#         elif A[i] < B[i]:
#             b += 3; win = 'B'
#         else:
#             a += 1; b += 1;    
#     print(a, b)
#     if a == b:
#         print(win)
#     else:
#         print('A' if a > b else 'B')
# 출력 시간은 비슷하나 코드 길이가 적다