import sys
sys.stdin=open('input/15230.txt', 'r')
testcase = int(input())
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(testcase):
    word = input()
    count = 0
    for index in range(len(word)):
        if word[index] != alpha[index]:
            print(f'#{i+1} {count}')
            break
        count +=1
        if index == len(word)-1:
            print(f'#{i+1} {count }')

        
