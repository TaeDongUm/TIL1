import sys
sys.stdin=open('input/14555.txt','r')

# testcase = int(input())
# for i in range(testcase):
#     word = input()
#     count =0
#     while '()' in word:
#         word = word.replace('()',' ')
#         count +=1
#     for j in word:
#         if '(' ==j:
#             count +=1
#         elif ')' ==j:
#             count +=1
#     print('#{} {}'.format(i+1, count))

# T = int(input())
# for tc in range(1, T+1):
#     s = input()
#     cnt = 0
#     for i in range(1, len(s)):
#         if s[i]==')':
#             cnt += 1
#         elif s[i-1]=='(' and s[i]=='|':
#             cnt += 1
#     print(f'#{tc} {cnt}')
testcase = int(input())
  
for i in range(testcase):
    word = input()
  
    result = 0
    j = 0
    while(j < len(word)):
        if word[j] == '(':
            if word[j + 1] == ')':
                result += 1
                j += 1
            else:
                result += 1
        elif word[j] == ')':
            result += 1
        j += 1
  
    print("#{} {}".format(i+1, result))