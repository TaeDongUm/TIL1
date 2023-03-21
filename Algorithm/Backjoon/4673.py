# N=10000
# sum_=0
# num=[]
# # *self_num=[True for _ in range(0,10000)]
# for i in range(1,10001):
#     n=i 
#     while 1:
#         units = n % 10
#         sum_+=units
#         n = n//10
#         if n==0:
#             break
#     if i + sum_ <=10000:
#         num.append(i+sum_)
#         # *self_num[i+sum_-1]=False
#     sum_=0
# num=list(set(num))
# for i in range(1,10001):
#     if i not in num:
#     # *if self_num[i] == True:
#         print(i)

N=10000
sum_=0
num=[]
self_num=[True for _ in range(0,10000)]
for i in range(1,10001):
    n=i 
    while 1:
        units = n % 10
        sum_+=units
        n = n//10
        if n==0:
            break
    if i + sum_ <=10000:
        # num.append(i+sum_)
        self_num[i+sum_-1]=False
    sum_=0
num=list(set(num))
for i in range(0,10000):
    if self_num[i] == True:
        print(i+1)
#(코드 길이 309 B) (메모리, 시간)=(31352 KB, 652 ms) 시간 줄이는 법?
# 리스트 append를 사용하기보다 아예 하나의 리스트(self_num)를 만들고 True로 10000번째까지 채운 후
# while문을 통해 나온 값과 self_num의 인덱스를 일치시키고 그 True값을 False로 변환시킴으로써 시간을 많이 줄일 수 있다.
# (코드 길이 393 B)	(84 ms ,30840  KB)


# num=[i for i in range(1,10001)]
# arr=[True]*10000

# for t in range(1,10001):
#     if 1<=t<=9:
#         arr[t+t-1]=False
#     elif 10<=t<=99:
#         arr[t+(t//10)+(t%10)-1]=False
#     elif 100<=t<=999:
#         arr[t+(t//100)+((t//10)%10)+(t%10)-1]=False
#     elif 1000<t<=9999:
#         if (t+(t // 1000)+((t//100)%10)+((t//10)%10)+(t%10)-1)>=10000:
#             continue
#         else:
#          arr[t+(t//1000)+((t//100)%10)+((t//10)%10)+(t%10)-1]=False


# for i in range(10000):
#     if arr[i]:
#         print(num[i])