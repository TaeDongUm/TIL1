Testcase = int(input())
def XOR(a, b):
    if a == 0:
        if b == 0:
            return 0
        elif b == 1:
            return 1
    elif a == 1:
        if b == 0:
            return 1
        elif b == 1:
            return 0
for k in range(Testcase):
    row, column = map(int,input().split())
    Matrix = []
    XOR_Matrix = [False for _ in range(row)]
    b_matrix=[]
    a_matrix=[]
    checking_matrix = []
    check_TF=[False for _ in range(row)]
    a_matrix_check =[False for _ in range(row)]
    ForBreak = False
    for row in range(row):
        Matrix.append(list(map(int,input().split())))
    for a in range(2):
        row1 = 0
        a_matrix[0] = a
        check_TF[0] = True
        a_matrix_check[0]= True
        # b 수열 구하기
        for column in range(column):
            if a == Matrix[row1][column]:
                b_matrix.append(0)
            else:
                b_matrix.append(1)
        # a 수열 2항부터 구하기
        for row2 in range(1, row):
            # a항이 0인지 1인지 구하기
            for a in range(2):
                for index in range(len(b_matrix)):
                    checking_matrix.append(XOR(a,b_matrix[index]))
                for index in range(len(Matrix)):
                    if checking_matrix[index] != Matrix[row2][index]:
                        break
                    else:
                        a_matrix_check[index] = True
                for value in range(len(a_matrix_check)):
                    if a_matrix_check[value] == False:
                        a_matrix_check =[False for _ in range(row)]
                        ForBreak = True
                        break
                    else:
                        check_TF[value] = True
            if ForBreak == True:
                ForBreak = False
                break
# 다시


                        


            
            






    