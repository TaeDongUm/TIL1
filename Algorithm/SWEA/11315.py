import sys
from collections import deque
sys.stdin = open('input/11315.txt','r')

T = int(input())
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for i in range(T):
    deque = deque()
    N= int(input())
    graph=[]
    for j in range(N):
        o_mok=input()
        graph.append(o_mok)
# 이어가기
