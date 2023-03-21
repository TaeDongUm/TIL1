N, X = map(int, input().split())
a= input().split()
for i in range(N):
    a[i] = int(a[i])
for i in range(len(a)):
    if a[i] >= X:
        a[i] = 0
remove_={0}
a_new=[i for i in a if i not in remove_]
for i in a_new:
    print(i, end=' ')




#이렇게 짜게 되면 문제 발생
# 입력 [1, 10, 4, 9, 2, 3, 8, 5, 7, 6] 이라면
# for문은 1->10->4->9-> 이 순서로 돌리다가
# remove 때문에 1->10->9->3->8->7 이 순서로 반복문이 돌게 된다
# 즉, remove로 인해 리스트가 변경이 됐는데 반복문을 통해 보는
# 인덱스는 a[0]a[1]a[2]a[3] 순서로 보기 때문

# N, X = map(int, input().split())
# a= input().split()
# print(X)
# print(a)
# for i in range(N):
#     a[i] = int(a[i])
# print(a)
# for i in a:
#     if i >= X:
#         a.remove(i)
#     print("1")
# print(a)
