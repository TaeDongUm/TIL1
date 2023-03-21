import sys
sys.stdin=open("input/2309.txt")
# height=[]
# for i in range(9):
#     height.append(int(input()))
# sum_=sum(height)
# print(sum_)
# ForBreak=True
# for i in range(8):
#     for j in range(i+1,9):
#         if 100 == sum_-(height[i]+height[j]):
#             height.pop(i)
#             height.pop(j)   # 먼저 i를 지우게 된 후 전체 인덱스가 줄어든 상태에서 j를 지우게 되면
#             ForBreak=False  # 의도했던 j가 지워지지 않게 됨.
#             break
#     if ForBreak ==False:
#         break
# height_=sorted(height)
# for i in range(len(height)):
#     print(height[i])

# height=[]
# for i in range(9):
#     height.append(int(input()))
# sum_=sum(height)
# ForBreak=True
# for i in range(8):
#     for j in range(i+1,9):
#         if 100 == sum_-(height[i]+height[j]):
#             num1 = height[i]
#             num2 = height[j]
#             height.remove(num1)     # height[i] 지운 순간 height는 조정되지만 j는 바뀌지 않음
#             height.remove(num2)     # 그래서 25가 지워져야 하는데 다른 값이 지워짐
#             ForBreak=False  
#             break
#     if ForBreak ==False:
#         break
# height_=sorted(height)
# for i in range(len(height_)):
#     print(height_[i])

height=[]
for i in range(9):
    height.append(int(input()))
sum_=sum(height)
ForBreak=True
for i in range(8):
    for j in range(i+1,9): 
        if 100 == sum_-(height[i]+height[j]): # 여기서 문제는 break를 해도 처음 for문을 다시 들어감
            num1 = height[i]   # 그럼 if문을 다시 들어가게 되는데 remove로 height이 바뀌게 됨
            num2 = height[j]
            height.remove(num1)     
            height.remove(num2)
            ForBreak=False
            break
    if ForBreak==False:
        break         
height_=sorted(height)
for i in height_:
    print(i)
