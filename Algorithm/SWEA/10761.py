import sys
from collections import deque
sys.stdin = open('input/10761.txt','r')

TC = int(input())
for i in range(TC):
    deque1 = deque()
    second = 0
    work = list(input().split())
    b_location =1
    o_location=1
    b_second=0
    o_second=0
    # work의 첫번째항은 눌러야하는 버튼 횟수
    button=work[0]
    # work 리스트 하나하나씩 살펴보기
    # 리스트의 맨마지막은 버튼 번호이기 때문에 -1 해줌
    for j in range(len(work)-1):
        # 이전 값이 B이냐 O이냐 판단하기 위해서 deque1을 사용
        if deque1:
            last_robot=deque1.popleft()
        else:
            last_robot =''
            pass
        # 이전 로보트 이동이 있을 때 그 시간만큼 다른 로보트가 움직일 수 있음
        # 홀수가 B인지 O인지 판단하는 값
        # 짝수가 눌러야 하는 버튼 번호
        if j ==0:
            continue
        if j %2 !=0:
            # 현재 움직여야 하는 로보트가 B이냐 O이냐
            if j == 'B':
                # 이전에 움직인 로보트가 B이냐 O이냐 처음으로 움직이냐 판단
                if last_robot == 'B':
                    b_second += abs(int(work[j+1])-b_location) +1
                    second +=abs(int(work[j+1])-b_location) +1
                    b_location = int(work[j+1])
                    deque1.append('B')
                # 이전에 움직인 로보트가 O이면 O가 움직인 시간을 고려해야 함
                elif last_robot == 'O':
                    if o_second >= (int(work[j+1])-b_location+1):
                        b_second =1
                        b_location = int(work[j+1])
                        second +=1
                        o_second =0
                        deque1.append('B')
                    else:
                        second += (int(work[j+1]) - b_location +1) -o_second
                        b_second += (int(work[j+1]) - b_location +1) -o_second
                        b_location = int(work[j+1])
                        o_seond=0
                        deque1.append('B')
                # 이전에 움직인 로보트가 없고 처음으로 움직인다면
                elif last_robot == '':
                    b_second +=int(work[j+1]) - b_location +1
                    b_location = int(work[j+1])
                    second +=abs(int(work[j+1])-b_location) +1
                    deque1.append('B')
            elif j == 'O':   
                  # 이전에 움직인 로보트가 B이냐 O이냐 처음으로 움직이냐 판단
                if last_robot == 'B':
                    if b_second >= (int(work[j+1])-o_location+1):
                        o_second =1
                        o_location = int(work[j+1])
                        second +=1
                        b_second=0
                        deque1.append('O')
                        print(second,'33333')
                    else:
                        second += (int(work[j+1]) - o_location +1) -b_second
                        o_second += (int(work[j+1]) - o_location +1) -b_second
                        o_location = int(work[j+1])
                        deque1.append('O')
                # 이전에 움직인 로보트가 O이면 O가 움직인 시간을 고려해야 함
                elif last_robot == 'O':
                    o_second += abs(int(work[j+1])-o_location) +1
                    second +=abs(int(work[j+1])-o_location) +1
                    o_location = int(work[j+1])
                    b_second=0
                    deque1.append('O')
                # 이전에 움직인 로보트가 없고 처음으로 움직인다면
                elif last_robot == '':
                    o_second +=int(work[j+1]) - o_location +1
                    o_location = int(work[j+1])
                    deque1.append('O')
                    second +=abs(int(work[j+1])-o_location) +1
    print(f'#{i+1} {second}')

