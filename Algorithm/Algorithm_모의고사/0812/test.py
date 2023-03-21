dx=[-1,0,1,0]
dy=[0,1,0,-1]
row=0
column=0
for j in range(4):
    if (0<=(row+dx[j])<=4) and (0<=(column+dy[j])<=4):
        print(row+dx[j],column+dx[j])
        print('aaaaaaaaa')
