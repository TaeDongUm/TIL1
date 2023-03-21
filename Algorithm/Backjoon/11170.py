import sys
input=sys.stdin.readline

T = int(input())
for i in range(T):
    # cnt=0
    # N,M=map(int, input().split())
    # for j in range(N,M+1):
    #     while 1:
    #         n1 =j%10
    #         if n1==0:
    #             cnt+=1
    #         j = j//10
    #         if j==0:
    #             break
    # print(cnt)
    cnt =0
    N,M =input().split()
    for i in range(int(N), int(M)+1):
        for j in range(len(str(i))):
            string = str(i)
            if '0' in string[j]:
                cnt +=1
    print(cnt)

#     T = int(input())

# for t in range(T) :
#     a, b = list(map(int, input().split()))
#     result = 0
#     for i in range(a, b+1) :
#         result += str(i).count('0')

#     print(result)
# 그냥 str으로 바꾸고 count하면 시간이 많이 줄어듦