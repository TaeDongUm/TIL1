# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
# apple

word = 'apple'
word_list=list(word)
for i in word_list:
    if i =='a':
        word_list.remove('a')
        continue
new_word = ''.join(word_list)
print(new_word)
