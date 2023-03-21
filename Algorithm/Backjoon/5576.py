import sys
sys.stdin=open("input/5576.txt")

W_score=[]
K_score=[]
for i in range(10):
    score=int(input())
    W_score.append(score)
for j in range(10):
    score= int(input())
    K_score.append(score)
W_score=sorted(W_score, reverse=True)
K_score=sorted(K_score, reverse=True)
W__score=0
K__score=0
for m in range(3):
    W__score+=W_score[m]
    K__score+=K_score[m]
print(W__score, K__score, sep=' ')
