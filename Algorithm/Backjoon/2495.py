
import sys
sys.stdin=open("input/2495.txt")
cnt=0
check=0
length=[]
for i in range(3):
    number=input()
    cnt=0
    length=[]
    check=0
    for k in range(len(number)-1):
        if number[k] == number[k+1]:
            cnt+=1
            if k == len(number)-2:
                cnt+=1
                length.append(cnt)
        else:
            check+=1
            cnt+=1
            length.append(cnt)
            cnt=0
    if check ==8:
        print(1)
    else:
        print(max(length))
# 초기화 시키는 것 자주 까먹음!!

# 짧게 짠 다른 사람 코딩
# for _ in range(3):
#     arr = input()   # 입력값이 str이라고 생각했는데 아닌가?
#     number = 0
#     max_number = []
#     cnt = 1

#     for i in arr:
#         if i != number:
#             number = i
#             max_number.append(cnt)
#             cnt = 1
#         elif i == number:
#             cnt += 1
#     max_number.append(cnt)
    
#     print(max(max_number))
