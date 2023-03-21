# 촌수 계산
n= int(input())
start, end= list(map(int, input().split()))
m=int(input())

# _ 의미는 값을 사용하지 않겠다. 그냥 반복만 하겠다
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=list(map(int, input().split()))
    # 무방향 인접 그래프
    graph[x].append(y)
    graph[y].append(x)

visited=[False]*(n+1)

# dfs를 시작하기 위해서 기본값 설정(스택,)
# ^ 스택에 값을 추가할 때 촌수도 같이 추가(튜플의 형태로)
stack=[]
stack.append((start,0))
visited[start]=True
# 문제에 주어진 조건
answer=-1
# 스택이 비어있지 않으면 반복함
while len(stack) !=0:
    # 번호와 촌수를 같이 pop
    number, count =stack.pop()

    # pop을 한 값이 우리가 원하는 값(end)
    # 촌수가 연결이 안되어 있으면 line 29~ line 31 실행 X
    if number == end:
        answer =count
        break
    # 해당하는 값의 인접 그래프를 저장
    adj_graph=graph[number]

    # 인접하는 값들을 탐색
    for adj_number in adj_graph:
        # 방문한 적이 없을 때만 스택에 값을 append
        if not visited[adj_number]:
            # 인접 번호와 촌수를 같이 append
            # 이전 촌수값에서 +1하고 append
            stack.append(adj_number, count + 1)
            visited[adj_number] =True
# 촌수 계산은 어떻게 하면 될까?