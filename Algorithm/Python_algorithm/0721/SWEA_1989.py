T = int(input())
words_list=[]
for i in range(T):
    words = list(input())
    words_list.append(words)
for i in range(len(words_list)):
    while 1:
        j = 0
        if len(words_list[i]) % 2 == 0:
            if words_list[i][j] == words_list[i][len(words_list[i])-1]:
                words_list[i].pop(0)
                words_list[i].pop(len(words_list[i])-1)
                if len(words_list[i]) == 0:
                    print(f'#{i+1} 11')
                    break
            else:
                print(f'#{i+1} 02')
                break

        elif len(words_list[i]) % 2 != 0:
            if len(words_list[i]) != 1:
                if words_list[i][j] == words_list[i][len(words_list[i])-1]:
                    words_list[i].pop(0)
                    words_list[i].pop(len(words_list[i])-1)
                else:
                    print(f'#{i+1} 03')
                    break
            else:
                print(f'#{i+1} 14')
                break