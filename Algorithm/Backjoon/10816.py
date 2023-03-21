import sys
sys.stdin=open("input/10816.txt")

N=int(input())
N_list=list(map(int, input().split()))
M=int(input())
M_list=list(map(int, input().split()))
dic={}
for i in N_list:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in M_list:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')
# for i in range(M):
#     print(N_list.count(M_list[i]), end=' ')
#     if M_list[i] in N_list:
#         N_list.remove(M_list[i])
# print(N_list)
# ! 문제에서 주어진 갯수는 N_list, M_list 각각 인덱스 갯수가 1000만개이다. 즉, 이중 for문이면 1000만 * 1000만이게 된다.
# ! 시간 초과가 나지 않기 위해서 dictionary를 이용함