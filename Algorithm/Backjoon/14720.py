T=int(input())
milk=list(map(int,input().split()))
check_list=[]
check_=0
for i in range(T):
    if milk[i]==check_%3:
        check_+=1
print(check_)



# check=1         # 처음 0이 올 때만 확인하는 변수
# check_=0
# for i in range(T):
#     if milk[i]==0:
#         if check==1:
#             check_list.append(milk[i])
#             check-=1
#             cnt+=1
#             continue
#         else:
#             check_=check_list[-1]
#             if check_==2:
#                 cnt+=1
#                 check_list.append(milk[i])
#                 continue
#     elif milk[i]==1:
#         if check_list==[]:
#             continue
#         check_=check_list[-1]
#         if check_==0:
#             cnt+=1
#             check_list.append(milk[i])
#     elif milk[i]==2:
#         if check_list==[]:
#             continue
#         check_=check_list[-1]
#         if check_==1:
#             cnt+=1
#             check_list.append(milk[i])
# print(cnt)