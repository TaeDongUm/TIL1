N, M = map(int, input().split()) # N=교과서 수 , M= 더미 수
book_number=[]
Order_list=[]
for i in range(1,M+1):
    dummy_books=int(input())
    book_order=list(map(int, input().split()))
    book_number.append(dummy_books)
    Order_list.append(book_order)
CompareNum=[]
Takeout=[]
ForBreak=True
for j in range(N):
    if len(Order_list)==1:
        for k in range(len(Order_list[0])):
            Takeout.append(Order_list[0][k])
        for m in range(1,len(Takeout)+1):
            if Takeout[m-1] !=m:
                ForBreak=False
                print("No")
                break
            elif Takeout[-1]==N:
                print("Yes")
                ForBreak==False
                break
        if ForBreak==False:
            break
    for i in range(len(Order_list)):  # [[9,7,4],[6,2,1],[8,5,3]]각 더미의 맨 위 번호 비교하기 위한 for문
        CompareNum.append(Order_list[i][-1])
    index=CompareNum.index(min(CompareNum))
    Takeout.append(Order_list[index][-1])   
    Order_list[index].pop()             
    if Order_list[index]==[]:
        Order_list.pop(index)
    CompareNum=[]
    for k in range(1,len(Takeout)+1):
        if Takeout[k-1] !=k:
            ForBreak=False
            print("No")
            break
        elif Takeout[-1]==N:
            print("Yes")
            ForBreak==False
            break
    if ForBreak==False:
        break
# Compare=[]
# for l in range(1,N+1):  # 교과서 수까지 수열 [1,2,3,4,5,......]
#     Compare.append(l)
# if Compare == Takeout:  # Takeout
#     print("Yes", end='')
# else:
#     print("No", end='')
