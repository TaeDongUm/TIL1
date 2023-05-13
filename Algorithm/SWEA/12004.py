T = int(input())
graph = [[] for _ in range(9)]
for i in range(9):
    for j in range(9):
        graph[i].append((i+1)*(j+1))
for i in range(T):
    N = int(input())
    count =0
    for j in range(9):
        if N in graph[j]:
            count +=1
    if count >=1:
        print(f'#{i+1} Yes')
    else:
        print(f'#{i+1} No')

# T=int(input())
# for t in range(T):
#     N=int(input())
#     result='No'
#     for i in range(1, 10):
#         if N%i==0:
#             if N/i<10:
#                 result='Yes'
#     print(f'#{t+1} {result}')