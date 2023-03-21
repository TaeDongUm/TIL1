import sys
sys.stdin=open("input/7785.txt")
# input=sys.stdin.readline 
# 이 코딩의 문제는 찾아보니 최근 파이썬의 경우 dic의 순서를 고려하도록 업데이트가 되었다면
# 이전 파이썬, 백준 사이트의 경우 그렇지 못해서 틀렸다고 뜨는 것 같음
# 그래서 dic 보다는 순서를 고려할 수 있는 것으로 풀어야 할 듯
# dic으로 sorted 해도 제대로 풀려서 생각이 틀렸음을 알 수 있었음
# 하지만, (코드 길이 374 B) (메모리, 시간)=(49028 KB, 4180 ms)로 메모리, 시간 크다.
# 잘하는 사람들은 보통 200 ~300 ms가 나오는 것을 확인
# 어떻게 줄일 수 있을까?
# input=sys.stdin.readline 
# 기존
N = int(input())
dic={}
for i in range(N):
    People=input().split()
    if People[0] not in dic:
        dic[People[0]]=1
    elif People[1] =='leave':
        dic[People[0]]+=1
    elif People[0] in dic:
        dic[People[0]]+=1
b=(sorted(dic.items(), reverse=True))
for i in range(len(b)):
    if b[i][1] %2 !=0:
        print(b[i][0])

# input=sys.stdin.readline 
#input=sys.stdin.readline  추가
# input에 .rstrip().split() 추가
input = sys.stdin.readline
N = int(input())
dic={}
for i in range(N):
    People=input().rstrip().split()
    if People[0] not in dic:
        dic[People[0]]=1
    elif People[1] =='leave':
        dic[People[0]]+=1
    elif People[0] in dic:
        dic[People[0]]+=1
b=(sorted(dic.items(), reverse=True))
for i in range(len(b)):
    if b[i][1] %2 !=0:
        print(b[i][0])
# (코드 길이 387 B) =(메모리, 시간) = (49028 KB, 284 ms)로 시간이 대폭 줄었음

N=int(input())
enter=[]
for i in range(N):
    People=input().split()
    if People[1]=='enter':
        enter.append(People[0])
    elif People[1]=='leave':
        enter.remove(People[0])
enter=sorted(enter, reverse=True)

for i in range(len(enter)):
    print(enter[i])
# 리스트의 경우 sys.stdin.readline().split()을 해도 시간 초과
# 리스트로 풀려고 했는데 NameError가 뜸
# 
# input=sys.stdin.readline
# N=int(input())
# enter=[]
# for i in range(N):
#     People=input().rstrip().split()
#     if People[1]=='enter':
#         enter.append(People[0])
#     elif People[1]=='leave':
#         enter.remove(People[0])
# enter=sorted(enter, reverse=True)

# for i in range(len(enter)):
#     print(enter[i])

# print(sorted(['a','A','b','B','c','C'], reverse=True))


