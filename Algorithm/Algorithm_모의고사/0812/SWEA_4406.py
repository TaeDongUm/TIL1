import sys
sys.stdin=open("input/4406.txt")

T=int(input())
for i in range(T):
    word=input()
    word=word.replace('a','')
    word=word.replace('e','')
    word=word.replace('i','')
    word=word.replace('o','')
    word=word.replace('u','')
    print(f'#{i+1} {word}')


# 안되는 이유?
# T=int(input())
# for i in range(T):
#     word=input()
#     for j in range(len(word)):   # replace는 기존 변수에 저장되지 않고 반환하는 함수임
#         word.replace('a','') 
#         word.replace('e','')
#         word.replace('i','')
#         word.replace('o','')
#         word.replace('u','')
#         print(word)
    
