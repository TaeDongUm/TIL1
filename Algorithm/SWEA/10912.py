import sys
sys.stdin = open('input/10912.txt','r')

T = int(input())
for i in range(T):
    s = input()
    word = ''.join(sorted(s))
    word1 =list(set(word))
    for j in range(len(word1)):
        if word.count(word1[j]) <2:
            pass
        elif word.count(word1[j])%2==0:
            word = word.replace(word1[j],'',word.count(word1[j]))
        else:
            word= word.replace(word1[j], '', word.count(word1[j])-(word.count(word1[j])%2))
    if word =='':
        print('#{} Good'.format(i+1))
    else:
        print('#{} {}'.format(i+1, word))

# a = int(input())
# for k in range(1,a+1):
#     b = list(str(input()))
#     list1 = []
#     for i in b:
#         if i not in list1:
#             list1.append(i)
#         else:
#             list1.remove(i)
#     list1.sort()
#     if len(list1) == 0:
#         print(f'#{k}','Good')
#     else:
#         print(f'#{k}',''.join(list1))

# T=int(input())
# for t in range(T):
#     S=sorted(input().rstrip())
#     st=[0]
#     for s in S:
#         if st[-1]==s:
#             st.pop()
#         else:
#             st.append(s)
#     if len(st)==1:
#         print(f'#{t+1} Good')
#     else:
#         S=''.join(st[1:])
#         print(f'#{t+1} {S}')

# 코드 차이는 크게 없는 것 같은데 실행시간이 빠르다.
# T = int(input())
# res = []
  
# for test_case in range(1, T + 1):
#     st = input()
#     arr = []
 
#     for s in st:
#         if s not in arr:
#             arr.append(s)
#         else:
#             arr.remove(s)
 
#     if len(arr) == 0:
#         arr = "Good"
#     else:
#         arr.sort()
#         arr = ''.join(arr)
#     res.append([test_case, arr])
 
# for idx, on in res:
#     print(f"#{idx} {on}")