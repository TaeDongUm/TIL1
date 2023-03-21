import sys
# N, M = map(int, input().split())
N, M = [int(x) for x in sys.stdin.readline().split()]
Order_list=[]
for i in range(1,M+1):
    dummy_books=int(sys.stdin.readline())
    # book_order=list(map(int, input().split()))
    book_order=[int(x) for x in sys.stdin.readline().split()]
    Order_list.append(book_order)
i=0
while 1:
    if Order_list[i] ==list(reversed(sorted(Order_list[i]))):
        i+=1
        if len(Order_list) == i:
            print("Yes")
            break
        continue
    else:
        print("No")
        break


# N, M = map(int, input().split())
# Order_list=[]
# for i in range(1,M+1):
#     dummy_books=int(input())
#     book_order=list(map(int, input().split()))
#     Order_list.append(book_order)
# Takeout=[][[3,1][4,2]......9만개[]]
# j=0
# k=1
# while 1:
#     if Order_list[j][-1]==k: 
#         Takeout.append(k)
#         del Order_list[j][-1]
#         if Order_list[j]==[]:
#             Order_list.pop(j)
#         k+=1
#         j=0
#         if len(Takeout)==N:
#             print("Yes")
#             break
#         continue
#     elif j==M-1:
#         print("No")
#         break
#     j+=1
# 처음에는 [[dummy1],[dumm2],[dummy3],[dummy4]]에서
# Order_list[j][-1]를 통해 각 dummy의 맨 뒤 자리를 보고
# 1부터 하나하나씩 파악하고 해당 자리 지우는 알고리즘을 짰는데 너무 비효율적
# Yes가 뜨기 위해선 각 dummy는 역순이어야 함
# 찾아보니 input에서 걸리는 시간을 줄이기 위해서 다음과 같이 짠다고 함
# N, M = [int(x) for x in sys.stdin.readline().split()]
# dummy_books=int(sys.stdin.readline())
# book_order=[int(x) for x in sys.stdin.readline().split()]