import sys
sys.stdin = open('input/9480.txt','r')

TC = int(input())
for i in range(TC):
    N = int(input())
    for j in range(N):

# alphabets = "abcdefghijklmnopqrstuvwxyz"
# def check(lst):
#     global cnt
#     total = 0
#     alphabet = set([])
#     for s in lst:
#         alphabet.update(set(s))
#     for i in alphabets:
#         if i in alphabet:
#             total +=1
#     if total == 26:
#         cnt += 1
# def subList(idx, step, lst):
#     if step == N+1:
#         check(lst)
#         return
#     tmp = lst[:]
#     lst.append(words[idx])
#     subList(idx+1, step+1, tmp)
#     subList(idx+1, step+1, lst)
# for tc in range(1, int(input())+1):
#     N = int(input())
#     words = []
#     cnt = 0
#     lst = []
#     for i in range(N):
#         words.append(input())
#     subList(0, 1, lst)
#     print('#{} {}'.format(tc, cnt))

# from itertools import combinations
# T = int(input())
# alpha_set = set(list('abcdefghijklmnopqrstuvwxyz'))
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N = int(input())
#     vocaes = list(input() for _ in range(N))
#     answer = 0
#     for i in range(1,N + 1):
#         for cases in combinations(vocaes, i):
             
#             if not (len(alpha_set - set(list(''.join(cases))))):
#                 answer += 1
#     print(f'#{test_case} {answer}')

# SW Expert Academy - 9480번. 민정이와 광직이의 알파벳 공부
# alphabets = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]
 
 
# def comb(idx, k, length):
#     global result
#     if k == length:
#         # 알파벳 검사
#         cnt = 0
#         string = ''.join(candi)
#         for alpha in alphabets:
#             if alpha in string:
#                 cnt += 1
#         if cnt == 26:
#             result += 1
 
#         return
 
#     for i in range(idx, N):
#         if not visited[i]:
#             visited[i] = True
#             candi.append(words[i])
#             comb(i, k + 1, length)
#             visited[i] = False
#             candi.pop()
 
 
# T = int(input())
 
# for tc in range(1, T + 1):
#     N = int(input())
#     words = []
#     result = 0
#     for _ in range(N):
#         words.append(input())
 
#     for i in range(1, N + 1):
#         visited = [False] * N
#         candi = []
#         comb(0, 0, i)
#     print('#{} {}'.format(tc, result))