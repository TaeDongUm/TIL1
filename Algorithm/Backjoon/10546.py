import sys
N=int(input())
dict={}
for i in range(2*N-1):
    people=sys.stdin.readline().strip()
    if people not in dict:
        dict[people]=1
    else:
        dict[people]+=1
for k,v in dict.items():
    if v%2 !=0:
        print(k)

# # 참가자 기록 및 완주자 체크
# N = int(input())
# participant = set()   # 참가자 명단
# for _ in range(2 * N - 1):
#     person = sys.stdin.readline().rstrip()
#     if person in participant:
#         participant.remove(person)
#     else:
#         participant.add(person)

# # 완주하지 못한 사람 출력
# print(*participant)
