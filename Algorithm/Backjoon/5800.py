import sys
sys.stdin=open("input/5800.txt")
K=int(input())
for i in range(K):
    score=list(map(int, input().split()))
    score.pop(0)
    for j in range(len(score)):
        Max= max(score)
        Min=min(score)
        score_reverse=sorted(score, reverse=True)
        temp=0
        for k in range(len(score_reverse)-1):
            diff = score_reverse[k]-score_reverse[k+1]
            if temp < diff:
                temp = diff
        Largest_gap = temp
        
    print(f'Class {i+1}')
    print(f'Max {Max}, Min {Min}, Largest gap {Largest_gap}')

#     # k = int(input())
# for i in range(k):
#     n = list(map(int,input().split(' ')))
#     t = n.pop(0)
#     n.sort(reverse=True)

#     gap = 0
#     for j in range(t-1):
#         if n[j] - n[j+1] > gap:
#             gap = n[j] - n[j+1]


#     print(f'Class {i+1}')
#     print(f'Max {n[0]}, Min {n[-1]}, Largest gap {gap}')

# 단순히 역순으로 만든 후 처음 항이 최대값, 마지막 항이 최소값임