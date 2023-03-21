import sys
sys.stdin=open('input/1302.txt')
T= int(input())
dic={}
for i in range(T):
    book=input()
    if book not in dic:
        dic[book]=1
    else:
        dic[book]+=1

max_=max(dic.values())
keys=[]
for k,v in dic.items():
    if v==max_:
        keys.append(k)
keys=sorted(keys)
print(keys[0])

# pi = {'a':3,'b':1,'c':4,'aa':1,'bb':5,'cc':9}
# pi_list = []
# for key, value in sorted(pi.items(), key=lambda x:(-x[1], x[0])):
#     print(key,":",value)
# cc : 9
# bb : 5
# c : 4
# a : 3
# aa : 1
# b : 1
# 똑같은 1의 value를 가지고 있는 aa와 b가 이름 순으로 정렬된 것은 

# 정렬조건이 -x[1] 이후의 x[0]까지로 다중조건으로 되어있기 때문이다.

# -x[1] : value값을 기준으로 내림차순(큰 값부터 정렬)

# x[0] : 1조건인 -x[1]정렬을 시행한 이후에 key값을 기준으로 오름차순(작은 값부터 or ABC순)
# [출처] 파이썬 딕셔너리 정렬 sorted(), key=lambda x: 다중조건|작성자 규

# import sys
# input = sys.stdin.readline
# n = int(input())
# book_dic = {}
# for _ in range(n):
#     book = input().rstrip()

#     # 책의 제목: key, 팔린 책의 갯수: value
#     if book in book_dic:
#         book_dic[book] += 1
#     else:
#         book_dic[book] = 1

# # 팔린 책의 갯수를 기준으로 내림차순 정렬, 만약, 책의 갯수가 같다면 제목을 사전순으로 출력
# # 최종적으로 제목 출력
# answer = sorted(book_dic.items(), key= lambda x : (-x[1], x[0]))
# #print(answer) [('top', 4), ('kimtop', 1)]
# print(answer[0][0])