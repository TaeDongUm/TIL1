N = int(input())
dash=''
for i in range(N):
    j = i+1
    while 1:
        n1 = j % 10
        j = j//10
        if (n1 == 3) or (n1 == 6) or (n1 == 9):
            dash += '-'
        if j == 0:
            break
    if dash != '':
        print(dash, end =' ')
    elif dash =='':
        print(i+1, end=' ')    
    dash =''
    
       
