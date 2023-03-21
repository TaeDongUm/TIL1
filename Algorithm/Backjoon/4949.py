import sys
from collections import deque
sys.stdin=open('input/4949.txt')
while 1:
    dq_1=[]
    sentence = sys.stdin.readline().rstrip()
    if sentence=='.':
        break
    else:
        for i in range(len(sentence)):
            if '(' ==sentence[i]:
                dq_1.append(sentence[i])
            elif '[' == sentence[i]:
                dq_1.append(sentence[i])
            elif ')' ==sentence[i]:
                if dq_1 and dq_1[-1] =='(':
                    dq_1.pop()
                else:
                    dq_1.append(')')
            elif ']' == sentence[i]:
                if dq_1 and dq_1[-1]=='[':
                    dq_1.pop()
                else:
                    dq_1.append(']')
        if len(dq_1) !=0:
            print("no")
        else:
            print("yes")
# (메모리 32452 KB)	(시간 428 ms) (코드 길이 740 B)
# sys.stdin.readline().rstrip()을 쓰면
# (메모리 32452 KB)	(시간 168 ms) (코드 길이 773 B)

# while 1:
#     sentence=sys.stdin.readline().rstrip()  # rstrip은 개행을 없애기 위한 것.  그냥 strip이면 케이스 7번째인 ' .' 뛰어쓰기가 사라지기 때문에 안됨
#     check=''
#     if sentence =='.':
#         break
#     for i in range(len(sentence)):
#         if sentence[i] == '(' or sentence[i]==')' or sentence[i] == '[' or sentence[i]==']':
#             check+=sentence[i]
#     while 1:
#         if '()' in check:
#             check=check.replace("()",'')
#         elif '[]' in check:
#             check=check.replace('[]','')
#         else:
#             break
#     if len(check) !=0:
#         print("no")
#     else:
#         print('yes')
#(메모리 30840 KB)	(시간 168 ms) (코드 길이 526 B)

