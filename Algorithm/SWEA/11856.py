T = int(input())

for i in range(T):
    S = input()
    count =0
    for j in range(4):
        if S.count(S[j]) != 2:
            continue
        elif S.count(S[j]) ==2:
            count +=1
    if count ==4:
        print(f'#{i+1} Yes')
    else:
        print(f'#{i+1} No')
# 메모리 58,484kb, 실행시간 148ms, 코드길이 279B

# T = int(input())
# for tc in range(1, T+1):
#     word = list(input())
#     let = list(set(word))
#     check = True
#     for i in let:
#         if word.count(i)!= 2:
#             check = False
#     if check:
#         print("#{} {}".format(tc, "Yes"))
#     else:
#         print("#{} {}".format(tc, "No"))
# 메모리 42,716kb, 실행시간 93ms, 코드길이 292B


# def halfhalf(s: str) -> str:
#     dict = {}
     
#     for x in s:
#         if x not in dict:
#             dict[x] = 1
#         else:
#             dict[x] += 1
     
#     if len(dict.keys()) == 2:
#         for _, value in dict.items():
#             if value != 2:
#                 return 'No'
#     else:
#         return 'No'
#     return 'Yes'
 
# T = int(input())
 
# for test_case in range(1, T + 1):
#     s = str(input())
#     print(f'#{test_case} {halfhalf(s)}')
# 메모리 42,192kb, 실행시간 94ms, 코드길이 443B