import sys
sys.stdin=open("input/1371.txt")
dic={}
while 1:
    # try:
    word=input()
    word=word.replace(' ','')
    for i in word:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    # except:
        # break
max_value=max(dic.values())
# dict_value={v:k for k,v in dic.items()}  # 기존 value값에 중복이 있다면 1개만 저장되는 문제가 발생
# dict_value=sorted(dict_value.items(), key= lambda x: x[1]) lambda를 이용해서 key값을 정렬함
# print(dict_value.get[max(dic.values())]) # 리스트를 get 함수 이용할 수 없음
key=[k for k,v in dic.items() if v ==max(dic.values())]
key=sorted(key)
for i in range(len(key)):
    print(key[i],end='')

# word_num=sorted(dic.items(), key =lambda x : x[1], reverse=True) # 리스트를 반환하는데 리스트는 value 함수를 사용할 수 없음
# values=word_num.values()
# print(values)

# import sys
# S = sys.stdin.read()

# list_=[0]*26
# for i in S:
#     if i.islower():
#         list_[ord(i)-97]+=1
# for j in range(26):
#     if list_[j]==max(list_):
#         print(chr(j+97),end='') 
# 이 분은 리스트를 통해 카운트했음