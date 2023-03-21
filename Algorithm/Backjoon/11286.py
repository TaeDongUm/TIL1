import sys
import heapq
sys.stdin=open("input/11286.txt")

# T=int(input())
# A=[]
# for i in range(T):
#     A.append(int(input()))
# cnt=0
# for i in A:
#     if i == 0:
#         cnt+=1

# # [1,-1,0,0,0,1,1,-1,-1,2,-2,0,0,0,0,0,0,0]
# # [1,-1,0,0,0,1,1,-1,-1,2,-2,0,0,0,0,0,0,0]
# i=0
# while cnt>0:
#     if A[i] < A[i+1]:
#         print(A[i])
#         del A[i]
#         if A[i] == 0 or A[i+1]==0:

#     elif A[i] > A[i+1]:
#         print(A[i+1])
#         del A[i+1]

#     cnt-=1
    

# T=int(input())[[3,-3],[-2,2],[1,-1],0,0,0,0,0,0] cnt=1 abs(stack[i]) abs_list.append(stack[i])
# A=[]
# abs_list=[] [1,-1] heapq.heappop abs_list=[]
# for i in range(T):
#     x=int(input())
#     print(x)
#     if x==0:
#         if A==[]:
#             print(A)
#             print(0,'aaaaa')
#         else:
#             j=0
#             A=sorted(A, key=abs) [1,-1] [1,-1,2,-2] [2,-2,-3,3]
#             cnt=1
#             while len(A) !=0:
#                 if abs(A[j]) ==cnt:
#                     abs_list.append(A[j])
#                     del A[j]
#                 else:
#                     if abs_list==[]:
#                         cnt+=1
#                         continue
#                     cnt+=1
#                     heapq.heapify(abs_list)
#                     for k in range(len(abs_list)):
#                         number=heapq.heappop(abs_list)
#                         print(number)
#     else:
#         A.append(x)
        
#         print('aaaaaaaaaa')
#         print(A,'bbbb')
# T=int(input())
# A=[]
# for i in range(T):
#     x = int(sys.stdin.readline())
#     if x !=0:
#         A.append(x)
#     elif x==0:
#         if A==[]:
#             print(0)
#         else:
#             A=sorted(A,key=lambda x:(abs(x)))
#             if abs(max(A)) <=abs(min(A)):
#                 index=abs(min(A))
#             else:
#                 index=abs(max(A))
#             abs_list=[[] for _ in range(index+1)]
#             for i in range(len(A)):
#                 abs_list[abs(A[i])].append(A[i])
#             # A=[]
#             for i in range(len(abs_list)):
#                 if abs_list[i]==[]:
#                     pass
#                 else:
#                     heapq.heapify(abs_list[i])
#                     num=abs_list[i][0]
#                     print(heapq.heappop(abs_list[i]))
#                     A.remove(num)
#                     break
            # for i in range(len(A)):
            # if A[0]>0:
            #     for i in A:
            #         if i<0 and abs(i)==A[0]: [1,1,1,1,-----90000개-----,-1] [1,1,1,1,-----90000개-----,-1,2,3,4----]
            #             print(i)
            #             A.remove(i)
            #             break
            #         elif abs(A[0]) < abs(i): [-1,1,-----90000개-----2,-2]
            #             print(A[0])
            #             del A[0]
            #             break
            #         elif max(A)==A[0]:
            #             heapq.heapify(A)
            #             print(heapq.heappop(A))
            #             break
            #         elif len(A)==1:
            #             print(A[0])
            #             del A[0]
            #             break
            # elif A[0]<0: 
            #     print(A[0])
            #     del A[0]

# input = sys.stdin.readline

# N = int(input())
# Q = []

# for _ in range(N):
#     num = int(input())


#     if num != 0:
#         if num < 0:
#             heapq.heappush(Q, [abs(num),-1])
#         else:
#             heapq.heappush(Q, [abs(num), 1])
#         print(Q)
#     else:
#         if Q:
#             temp, oper = heapq.heappop(Q)
#             print(temp*oper)
#         else:
#             print(0)
numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))  #튜플은 첫번째 요소를 기준으로 정렬이 된다. (만약 첫번째 요소 같으면, 두번째 요소로 넘어가는 방식)
        print(heap)
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)