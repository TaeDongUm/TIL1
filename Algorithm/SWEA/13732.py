import sys
sys.stdin = open('input/13732.txt','r')
T = int(input())
for i in range(T):
    N = int(input())
    graph=[]
    ForBreak = False
    for j in range(N):
        graph.append(list(input()))
        compare =[]
    for x in  range(N):
        x1 =-1
        y1=-1
        count = 1
        for y in range(N-1):
            if graph[x][y] == '#' and graph[x][y+1] == '#':
                count +=1
                x1, y1 = x, y
                if x<x1 and y<y1:
                    x1 = x
                    y1 = y
        if ((x1 >=0) and (y1 >=0) and (count > 1)):
            compare.append((x1,y1,count))
    count1=0
    count2=0
    if len(compare) !=0:
        row=[]
        length = compare[0][2]
        column = compare[0][1]
    else:
        row =[]
        length = 0
        column = 0
    for k in range(len(compare)):
        if compare[k][2] != length:
            print(f'#{i+1} no')
            ForBreak = True
            break
        elif compare[k][2] == length and compare[k][1] == column:
            row.append(compare[k][0])
            count1 +=1
    for l in range(len(row)-1):
        if row[l+1]-row[l] ==1:
            count2 +=1
    if ForBreak == True:
        continue
    if length == count1 and count1 !=0 and count2 == length-1:
        print(f'#{i+1} yes')
    else:
        print(f'#{i+1} no')
# 테케 20개 중 14개 맞음
    



