Testcase = int(input())
for k in range(Testcase):
    n, m = map(int,input().split())
    Matrix = []
    XOR_Matrix = False
    for i in range(n):
        row = list(map(int,input().split))
        Matrix.append(row)
    for i in range(m):
        a = 0
        b_matrix =[] 
        if a == Matrix[0][i]:
            b = 0
        else:
            b = 1
        b_matrix.append(b)
    for j in range(m):
        a=1
        if a == b_matrix[0][j]:
            b_matrix[0][j] = 0
        else:
            b_matrix[0][j] = 1
    for j in range(m):
        if Matrix[0][j] == b_matrix[0][j]:
            XOR_Matrix = True
    if XOR_Matrix == True:
        print(f'#{i+1} yes')
    else:
        print(f'#{i+1} no')


    