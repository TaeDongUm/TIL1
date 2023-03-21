import sys

sys.stdin = open("input2.txt")
command=[]                      # 명령어 여러개를 담기 위한 리스트
Password_list1=[]               # 원본 리스트를 나누기 위한 리스트1
Password_list2=[]               # 원본 리스트를 나누기 위한 리스트2
for testcase in range(10):
    command=[]                  # 초기화를 해줘야 테스트 케이스 당 
    Password_length=int(input()) # 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)
    Password = input().split()  # 두 번째 줄 : 원본 암호문
    def_num=int(input())        # 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)
    def_= input().split()    # 네 번째 줄 : 명령어
    idx1=0
    idx2=0
    def_1=[]
    for a in range(len(def_)):
        if def_[a] =='I':
            idx1=a
            idx2 = a+2 + int(def_[a+2])
            for b in range(idx1, idx2+1):
                def_1.append(def_[b])
            command.append(def_1) #[[def_],[def_],[def_],[def_],[def_].....] 이런 꼴
            def_1=[]
    for i in range(len(command)):  # 이 for문은 원본 리스트를 나누기 위한 과정. 예를 들어 원본 암호가 [123123, 234876, 888888]이고
        # if int(command[i][1]) ==0:
        #     Password_list1=[]
        #     Password_list2=Password
        #     for c in range(int(command[i][2])):
        #         Password_list1.append(command[i][c+3])
        #     for d in range(len(Password_list2)):
        #         Password_list1.append(Password_list2[d])
        #     Password=Password_list1
        #     Password_list1=[]                               #각각을 초기화
        #     Password_list2=[]   
        # elif int(command[i][1]) !=0:
        for j in range(int(command[i][1])):     # 첫번째 명령어가 [I, 1, 2, 111111, 222222]이면 command[i][1]은 1을 의미
            Password_list1.append(Password[j])  # 즉 Password_list1 =[123123]
        for k in range(int(command[i][1]),len(Password)):   # Pasword_list2=[234876, 888888]으로 원본 암호를 나눔
            Password_list2.append(Password[k])
        for l in range(int(command[i][2])):         # 첫번째 명령어 [I, 1, 2, 111111, 222222]에서 command[i][2]는 원본 암호에 추가할 숫자들의 갯수
            Password_list1.append(command[i][l+3]) # Password_list1에 추가할 숫자들을 추가함. 즉, 결과로 [123123, 111111, 222222]
        for m in range(len(Password_list2)):        # 바로 위 결과인 [123123, 111111, 222222]에 
            Password_list1.append(Password_list2[m]) # Password_list2를 append하면 [123123, 111111, 222222, 234876, 888888]
                                                    # 원본 암호에 숫자 추가 완료 
        Password=Password_list1                      # 새롭게 만든 암호를 Password에 넣음
        Password_list1=[]                               #각각을 초기화
        Password_list2=[]
    print(f'#{testcase+1}', end=' ')
    for n in range(10):
        print(Password[n], end=' ')
    print('')
# for i in range(len(command)):
#     print(command[i])
    