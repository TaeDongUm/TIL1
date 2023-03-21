T=int(input())
for i in range(T):
    Word =(input())
    word_reverse = Word[::-1]
    New_word=""
    for j in range(len(word_reverse)):
        if word_reverse[j] == 'b':
            New_word +='d'
        if word_reverse[j] == 'q':
            New_word +='p'
        if word_reverse[j] == 'p':
            New_word +='q'
        if word_reverse[j] == 'd':
            New_word +='b'
    print(f'#{i+1} {New_word}')   