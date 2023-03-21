import sys
sys.stdin=open("input/10798.txt")
Word=[]
for i in range(5):
    word=input()
    Word.append(word)
print(Word)
length=0
for i in range(5):
    if length < len(Word[i]):
        length = len(Word[i])
for i in range(5):
    if len(Word[i]) < length:
        for j in range(length-len(Word[i])):
            Word[i]+='-'
print(Word)
New_word=''
for j in range(len(Word[i])):
    for i in range(5):
        if Word[i][j]=='-':
            continue
        else:
            New_word += Word[i][j]
print(New_word)

# arr = []

# for _ in range(5):
#     T = list(input())
#     arr.append(T)


# for col in range(15):
#     for row in range(5):
#         if col < len(arr[row]):
#             print(arr[row][col], end='')  --> 해당 열 인덱스보다 출력하고자 하는 행의 문자열 길이가 클 경우 출력한다.
# col == len(arr[row])-1 이므로  
