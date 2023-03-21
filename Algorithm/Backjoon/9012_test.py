# x=5
# for i in range(x):
#     print(i)
#     x-=1
#     i-=1
#     print(i)
# PS='wordword'
# j=2
# PS = ''.join(PS[x] for x in range(len(PS)) if x != j+1)
# PS = ''.join(PS[x] for x in range(len(PS)) if x != 0)
# print(PS)

# PS='((()))))'
# num=PS.count('(')
# print(num)

# import sys
# sys.stdin=open("input_9012.txt",'r')

# T = int(input())
# PS=[]
# for i in range(T):
#     PS.append(input())
# ForBreak=False
# j=0
# print(PS[0])
# print(i)
# print(PS[i].count('(')%2 !=0)
# print(PS[i].count(')')%2 !=0)  # 왜 i값이 정의 되지 않았는데 True, False가 뜰까?
# for문 완료 후의 i값이 저장되어 있음

#따라서, i가 바뀌는 것을 반영하고 싶다면, for문보다 while문이 나을 수 있다.

# for문에서 x값이 바뀌더라도 range는 바뀌지 않는 것을 볼 수 있다.
# 여기서, for문의 i와 for문 안의 i는 독립적으로 출력되는 것을 확인할 수 있다.
#0 (for문 i)
# -1 (for문 내의 i)
# 1 (for문 i)
# 0 (for문 내의 i)
# 2 (for문 i)
# 1 (for문 내의 i)
# 3 (for문 i)
# 2 (for문 내의 i)
# 4 (for문 i)
# 3 (for문 내의 i)

# print(len([]))

# j=1
# PS='((()))'
# PS = ''.join(PS[x] for x in range(len(PS)) if x != j+1)
# PS= ''.join(PS[x] for x in range(len(PS)) if x != 0)
# print(PS)

word="()()"
text=word.replace("()","")
if text =='':
    print("aaaaaaaaa")
print(text)
while 1:
    test=word.replace("()", "")
    if test !='':
        word=test
    if test == '':
        break
    

print("YES")
