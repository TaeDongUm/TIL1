T=int(input())
for i in range(T):
    sum_=0
    a,b=map(int, input().split())
    if a==1:
        sum_+=5000000
    if 2<=a<=3:
        sum_+=3000000
    if 4<=a<=6:
        sum_+=2000000
    if 7<=a<=10:
        sum_+=500000
    if 11<=a<=15:
        sum_+=300000
    if 16<=a<=21:
        sum_+=100000
    if b==1:
        sum_+=5120000
    if 2<=b<=3:
        sum_+=2560000
    if 4<=b<=7:
        sum_+=1280000
    if 8<=b<=15:
        sum_+=640000
    if 16<=b<=31:
        sum_+=320000
    print(sum_)

# 리스트를 만들고 들어오는 값들을 인덱스로 생각하여 출력하게끔 만듦
# I=lambda:map(int,input().split())
# a=[500]+[300]*2+[200]*3+[50]*4+[30]*5+[10]*6+[0]*99
# b=[512]+[256]*2+[128]*4+[64]*8+[32]*16+[0]*99
# for _ in range(int(input())):
#     x,y = I()
#     print((a[x-1]+b[y-1])*10000)

