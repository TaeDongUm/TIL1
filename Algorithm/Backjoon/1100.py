import sys
sys.stdin=open('input/1100.txt','r')

Matrix=[list(input()) for i in range(8)]

cnt=0
for i in range(8):
    for j in range(4):
        if i % 2 ==0:
            if Matrix[i][2*j] =='F':
                cnt +=1
        elif i % 2 !=0:
            if Matrix[i][2*j+1] =='F':
                cnt +=1
print(cnt)
