import sys
sys.stdin = open('input/14692.txt','r')

testcase = int(input())
for i in range(testcase):
    N=int(input())
    win ='Alice'
    if N%2!=0:
        win ='Bob'
    print('#{} {}'.format(i+1, win))
