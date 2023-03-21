word=input()
check='CAMBRIDGE'
i=0
while 1:    
    if i < len(word):
        if word[i] in check:
            word=word.replace(word[i],'')
        else:
            i+=1
    else:
        break
print(word)