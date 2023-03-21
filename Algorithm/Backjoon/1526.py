N = int(input())
num=[]
for i in range(4,N+1):
    number=i
    while 1:
        n1=i%10
        if (n1 != 4) and (n1 != 7): # or로 묶게 되면 n1이 4여도 if문에서 or는 하나만 만족하면 참이므로 모든 i 경우에서 참 
            break                   # 그래서 and로 묶어야 함
        i=i//10
        if i==0:
            num.append(number)
            break
num=sorted(num, reverse=True)
print(num[0])

# n = int(input())
# i = 1;a = 0;b=1;
# while i:
#     if(i==100000000):break;
#     for j in range(b):
#         x = (int(bin(j)[2:])*3)
#         if((a*4)+x>n):
#             if(x==0):print(((a-(i//10))*4)+(int(bin(t)[2:])*3));i=0;break;
#             else:print((a*4)+(int(bin(t)[2:])*3));i=0;break;
#         t=j
#     a += i
#     b*=2
#     i *= 10
# 왜 이진수로 바꿔서 한 걸까? 45994587	jaeminc94	1526	맞았습니다!!	30840	72	Python 3	328	

N = int(input())


# while True:
#     a = True
#     for i in str(N):
#         if i != '4' and i != '7':
#             a = False
#             N -= 1
#     if a:
#         print(N)
#         break