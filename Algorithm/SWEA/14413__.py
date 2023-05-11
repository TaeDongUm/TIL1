import sys
from pprint import pprint
sys.stdin = open('input/14413.txt', 'r')
def checking_1(graph):
    TF = 'possible'
    ForBreak = False
    for N in range(len(graph)):
        for M in range(len(graph[N])):
            if (N+M) %2 ==0 and graph[N][M]=='#':
                continue
            elif (N+M)%2 !=0 and graph[N][M]=='.':
                continue
            elif graph[N][M]=='?':
                continue
            else:
                TF = 'impossible'
                ForBreak = True
                break
        if ForBreak == True:
            break
    return TF

def checking_2(graph):
    TF = 'possible'
    ForBreak = False
    for N in range(len(graph)):
        for M in range(len(graph[N])):
            if (N+M) %2 !=0 and graph[N][M]=='#':
                continue
            elif (N+M)%2 ==0 and graph[N][M]=='.':
                continue
            elif graph[N][M]=='?':
                continue
            else:
                TF = 'impossible'
                ForBreak = True
                break
        if ForBreak == True:
            break
    return TF

testcase = int(input())
for i in range(testcase):
    N, M = map(int, input().split())
    graph =[]
    for N in range(N):
        graph.append(list(input()))
    n = checking_1(graph)  
    m = checking_2(graph)
    if n == 'possible' or m == 'possible':
        print(f'#{i+1} possible ')
    else:
        print('#{} {}'.format(i+1, 'impossible' ))
    

