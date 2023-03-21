Word = input()
sum_=0
for i in range(len(Word)):
    if (Word[i] == 'A'or Word[i] == 'B'or Word[i] == 'C'):
        sum_ += 3
    if (Word[i] == 'D'or Word[i] == 'E'or Word[i] == 'F'):
        sum_ += 4
    if (Word[i] == 'G'or Word[i] == 'H'or Word[i] == 'I'):
        sum_ += 5
    if (Word[i] == 'J'or Word[i] == 'K'or Word[i] == 'L'):
        sum_ += 6
    if (Word[i] == 'M'or Word[i] == 'N'or Word[i] == 'O'):
        sum_ += 7
    if (Word[i] == 'P'or Word[i] == 'Q'or Word[i] == 'R'or Word[i] == 'S'):
        sum_ += 8
    if (Word[i] == 'T'or Word[i] == 'U'or Word[i] == 'V'):
        sum_ += 9
    if (Word[i] == 'W'or Word[i] == 'X'or Word[i] == 'Y'or Word[i] == 'Z'):
        sum_ += 10
print(sum_)

# if 문이 다 참으로 됨
# if 'a' == 'b' or 'c' or 'd':
#   print(1)
# 이렇게 or를 넣는 순간 1을 출력함
# 그래서 and로 바꿨음
# and로 바꾸니 WA 와 XB는 값이 같아야 하는데 0으로 출력됨
# Word[i] == 'a'or 'b' or 'c'  이렇게 코드를 짜면
# or 나 and는 Word[i] 와 'a', 'b', 'c'의 type값이 같냐 안같냐를 비교하는 것