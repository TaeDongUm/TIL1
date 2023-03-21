import sys
sys.stdin=open("input/1264.txt")
while 1:
    cnt=0
    word=input()
    if word=='#':
        break
    word=word.upper()
    for i in range(len(word)):
        if word[i]=='A' or word[i]=='E' or word[i]=='I' or word[i]=='O' or word[i]=='U':
            cnt+=1
    print(cnt)
