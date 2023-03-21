T = int(input())                # 테스트 case
check=[]                        
num=[]
check_test=[0,1,2,3,4,5,6,7,8,9]
test_case = 1
cnt  =0

for i in range(T):
    num1 = int(input())
    num.append(num1)
for i in num:
    k=1
    while 1:
        i1 = k*i
        i2 = k*i
        while 1:
            n = i1 % 10**(cnt+1)
            i1 = i1 - n
            n1 = n // 10**(cnt)
            check.append(int(n1))
            
            result=[]
            # check=list(set(check))
            for j in check:
                if j not in result:
                    result.append(j)                 
            #
            cnt += 1
            if check_test == sorted(result):
                print(f'#{test_case} {i2}')
                check.clear()
                break
            if i1 == 0:
                break
        

        cnt =0
        
        if check == []:
            break

        k += 1
    test_case += 1