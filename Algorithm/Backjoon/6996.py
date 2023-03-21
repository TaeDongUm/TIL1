T=int(input())
for i in range(T):
    word1, word2=input().split()
    word_1= sorted(word1)
    word_2=sorted(word2)
    if word_1==word_2:
        print(f'{word1} & {word2} are anagrams.')
    else:
        print(f'{word1} & {word2} are NOT anagrams.')    