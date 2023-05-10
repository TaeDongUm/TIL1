Testcase = int(input())
# 최소공배수 구해서 문자열 비교하기
for i in range(Testcase):
    word=list(input().split())
    x = len(word[0])
    y = len(word[1])
    # x를 무조건 큰 값으로 정하기
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    
    # x값이 최소공배수
    check_x = word[1]*(len(word[0])//x)
    check_y = word[0]*(len(word[1])//x)
    if check_x == check_y:
        print(f'#{i+1} yes')
    else:
        print(f'#{i+1} no')
        
