from collections import deque
import sys
sys.stdin = open('input/10804.txt','r')

T= int(input())
for i in range(T):
    deque1=deque(input())
    list = []
    while len(deque1)>=1:
        check=deque1.pop()
        if   check =='b':
            list.append('d')
        elif check =='d':
            list.append('b')
        elif check =='p':
            list.append('q')
        elif check =='q':
            list.append('p')
    list1=''.join(list)
    print('#{} {}'.format(i+1,list1))

# T =int(input())
# for test_case in range(1, T+1):
#     word = input()
#     newWord = ""
#     word = word[::-1]
#     for w in word:
#         if w=="b": newWord+="d"
#         elif w=="d": newWord+="b"
#         elif w=="p": newWord+="q"
#         elif w=="q": newWord+="p"
#     print(f"#{test_case} {newWord}")