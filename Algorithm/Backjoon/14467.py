N= int(input())
Cow=[[] for i in range(N+1)]
for i in range(N):
    cow_number=list(map(int,input().split()))
    Cow[cow_number[0]].append(cow_number[1])
cnt=0
for i in range(1,N+1):
    if len(Cow[i])<=1:
        continue
    for k in range(len(Cow[i])-1):
        if Cow[i][k] != Cow[i][k+1]:
            cnt+=1
print(cnt)

# ! 딕셔너리로 깔끔하게 푼 다른 사람 코딩
# n = int(input())
# dict_ = {}
# cnt = 0
# for i in range(n):
#     n, l = map(int, input().split())
#     if n in dict_:
#         if dict_[n] != l:
#             cnt += 1
#     dict_[n] = l
# print(cnt)

