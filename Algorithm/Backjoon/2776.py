import sys
sys.stdin=open('input/2776.txt')
T=int(input())
for i in range(T):
    dict1={}
    note1_num=int(input())
    note1_list=list(map(int, input().split()))
    note2_num=int(input())
    note2_list=list(map(int, input().split()))
    for j in range(note1_num):
        if note1_list[j] not in dict1:
            dict1[note1_list[j]]=1
        else:
            dict1[note1_list[j]]+=1
    # for k in range(note2_num):
    #     if note2_list[k] not in dict2:
    #         dict2[note2_list[k]]=1
    #     else:
    #         dict2[note2_list[k]]+=1
    # print(dict2.keys())
    for m in note2_list:
        if m in dict1:
            print(1)
        else:
            print(0)

# import sys
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     note1 = set(input().split())
#     m = int(input())
#     note2 = input().split()
#     print('\n'.join('1' if i in note1 else '0' for i in note2))
# 코드 길이가 짧으면서 시간도 빠름