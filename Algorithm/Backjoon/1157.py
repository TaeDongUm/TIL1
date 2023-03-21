
# 리스트로 풀 경우
# word = input()
#  cnt=0
# Word=word.upper()
# num=list(set(Word))
# Count=[]
# for j in num:
#     for k in range(len(Word)):
#         if j==Word[k]:
#             cnt += 1
#     Count.append(cnt)
#     cnt=0
# for m in range(len(Count)):
#     if max(Count) == Count[m]:
#         cnt+=1
#     if cnt >1:
#         print("?")
#         break
# if cnt ==1:
#     index = Count.index(max(Count))
#     print(num[index], end='')
# (코드길이= 388B) (시간, 메모리) = (3248ms, 32796KB) 많이 길다.


#딕셔너리로 풀 경우
# word=input()
# Word = word.upper()
# dic={}
# for i in range(len(Word)):
#     if Word[i] not in dic:
#         dic[Word[i]]=1
#     else:
#         dic[Word[i]]+=1
# num=[k for k,v in dic.items() if v == max(dic.values())]
# if len(num)>1:
#     print("?",end='')
# else:
#     print(*num,end='')
# (코드길이= 273B) (시간, 메모리) = (328ms, 32796KB) 많이 줄었다. 그 이유는?




