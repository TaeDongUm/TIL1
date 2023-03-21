word = input()
num =0
for i in word:
    num += 1
    word = word[1:]

print(num)

# 다른 풀이 참고
"""
word = "happy!"

t = 0
while(word!=""):
    t+=1
    word = word[1:]
print(t)
"""