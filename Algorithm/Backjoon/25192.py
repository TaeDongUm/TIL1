import sys
sys.stdin=open('input/25192.txt')
# T=int(input())
# stack=[]
# cnt=0
# for i in range(T):
#     user=input()
#     if user =='ENTER':
#         if len(stack) !=0:
#             cnt += len(set(stack))-1
#             stack=[]
#     stack.append(user)
#     if i == T-1:
#         cnt += len(set(stack))-1
#         stack=[]
# print(cnt)
# 리스트로 풀어보니 시간이 많이 걸림 대략 3888ms

# 딕셔너리로 푼다면?
# 딕셔너리로 풀어보니 시간이 똑같이 많이 걸림 대략 3860ms
# ! 여기서 문제는 역시 sys.stdin.readline().rstrip()와 input()의 차이였음
T=int(input())
dict={}
cnt=0
for i in range(T):
    user=sys.stdin.readline().rstrip()
    if user=='ENTER':
        if len(dict.keys()) !=0:
            cnt += len(dict.keys())
            dict={}
    else:
        if user not in dict:
            dict[user]=1
        else:
            dict[user]+=1
    if i ==T-1:
        cnt += len(dict.keys())
print(cnt)
            