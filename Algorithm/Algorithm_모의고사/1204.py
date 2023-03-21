import sys
sys.stdin=open("input.txt",'r')
cnt=[]
cnt_num=0
Testcase=int(input())
Testcase_list=[]
num_list=[]
new_score=[]
for i in range(Testcase):
    score=[]
    cnt=[]
    Testcase_num=int(input())
    score=list(map(int, input().split()))
    for value in score:
        if value not in new_score:
            new_score.append(value)
    for j in new_score:
        for k in score:
            if j == k:
                cnt_num +=1
        cnt.append(cnt_num)
        cnt_num=0
    Testcase_list.append(list (new_score))
    num_list.append(cnt)
for i in range(len(num_list)):
    compare=0
    idx=0
    for j in range(len(num_list[i])):   
        if j == len(num_list[i])-1:
            break
        if num_list[i][j]  >= compare:
            compare = num_list[i][j]
            idx = j
        if num_list[i][j] < compare:
            compare = compare
    # if i ==2:
    #     print(idx)
    print(f'#{i+1} {Testcase_list[i][idx]}')
# print(num_list[2])
# print(Testcase_list[2])
        # if num_list[i][j] == compare:
        #     idx=j
# print(len(num_list[2]))

# 10개 테스트 케이스 중에서 9개 맞음
# 테스트 케이스 3에서 오류 발생
# vs code에서는 테스트 케이스 3 ==> 79로 뜨는데 똑같은 코드를  SWEA에 복붙했더니 77로 뜸
##=======================================================================================================

# SWEA 사이트 set 함수 안먹힘
