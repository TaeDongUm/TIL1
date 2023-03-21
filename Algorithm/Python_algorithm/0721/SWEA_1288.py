# T = int(input())
# check=[]
# num=[]
# check_test=[0,1,2,3,4,5,6,7,8,9]
# test_case = 1
# cnt  =0
# for i in range(T):
#     num1 = int(input())
#     num.append(num1)
# for i in num:
#     k=1
#     while 1:
#         i1 = k*i
#         i2 = k*i
#         while 1:
#             n = i1 % 10**(cnt+1)
#             i1 = i1 - n
#             n1 = n // 10**(cnt)
#             check.append(int(n1))
#             print(check)
#             check=list(set(check))
#             cnt += 1
#             if i1 == 0:
#                 break 
#         cnt =0
        
#         if check_test == check:
#             print(f'#{test_case} {i2}')
#             check.clear()
            
#             break
#         k += 1
#     test_case += 1

# 아래 코드는 시간 초과
# T = int(input())
# check=[]
# num=[]
# check_test=[0,1,2,3,4,5,6,7,8,9]
# test_case = 1
# cnt  =0
# for i in range(T):
#     num1 = int(input())
#     num.append(num1)
# for i in num:
#     k=1
#     while 1:
#         i1 = k*i
#         while 1:
#             n = i1 % 10**(cnt+1)
#             i2 = i1 - n
#             n1 = n // 10**(cnt)
#             check.append(int(n1))
#             print(check)
#             check=list(set(check))
#             cnt += 1
#             if i2 == 0:
#                 break 
#         cnt =0
        
#         if check_test == check:
#             print(f'#{test_case} {i1}')
#             check.clear()
            
#             break
#         k += 1
#     test_case += 1

T = int(input())
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
            print(check)
            check=list(set(check))
            cnt += 1
            if check_test == check:
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

# T = int(input())
# check=[]
# num=[]
# check_test=[0,1,2,3,4,5,6,7,8,9]
# test_case = 1
# cnt  =0
# for i in range(T):
#     num1 = int(input())
#     num.append(num1)
# for i in num:
#     k=1
#     while 1:
#         i1 = k*i
#         i2 = k*i
#         while 1:
#             n = i1 % 10**(cnt+1)
#             i1 = i1 - n
#             n1 = n // 10**(cnt)
#             check.append(int(n1))
#             print(check)
#             check=list(set(check))
#             cnt += 1

#             if i1 == 0:
#                 break
#         cnt =0
        
#         if check_test == check:
#             print(f'#{test_case} {i2}')
#             check.clear()
#             break
#         k += 1
#     test_case += 1