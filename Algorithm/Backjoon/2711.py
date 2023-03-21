import sys
sys.stdin=open('input/2711.txt')
T = int(input())
Typo=[]
for i in range(T):
    word = input().split()
    Typo.append(word)
for i in range(len(Typo)):
    temp=Typo[i][1]    
    temp=temp[:int(Typo[i][0])-1]+temp[int(Typo[i][0]):]
    print(temp)