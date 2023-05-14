from collections import deque
import sys
sys.stdin = open('input/10804.txt','r')

deque1 = deque()
T= int(input())
for i in range(T):
    deque1.append(list(input()))
    print(deque1)
    # for j in word:
    #     if j =='b':

    #     elif j =='d'
    #     elif j =='p'
    #     elif j =='q'