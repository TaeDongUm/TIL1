# 문제
# 상근이는 트럭을 총 세 대 가지고 있다. 오늘은 트럭을 주차하는데 비용이 얼마나 필요한지 알아보려고 한다.

# 상근이가 이용하는 주차장은 주차하는 트럭의 수에 따라서 주차 요금을 할인해 준다.

# 트럭을 한 대 주차할 때는 1분에 한 대당 A원을 내야 한다.
#  두 대를 주차할 때는 1분에 한 대당 B원, 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.

# A, B, C가 주어지고, 상근이의 트럭이 주차장에 주차된 시간이 주어졌을 때,
#  주차 요금으로 얼마를 내야 하는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문제에서 설명한 주차 요금 A, B, C가 주어진다. (1 ≤ C ≤ B ≤ A ≤ 100)

# 다음 세 개 줄에는 두 정수가 주어진다. 이 정수는 상근이가 가지고 있는 트럭이 주차장에 도착한 시간과 주차장에서 떠난 시간이다.
#  도착한 시간은 항상 떠난 시간보다 앞선다. 입력으로 주어지는 시간은 1과 100사이 이다.

# 출력
# 첫째 줄에 상근이가 내야하는 주차 요금을 출력한다.

# 5 3 1
# 1 6
# 3 5
# 2 8
A,B,C =map(int, input().split())
hour=[]

for i in range(3):
    use=list(map(int, input().split()))
    hour.append(use)
# print(hour)
start=min(hour[0][0],hour[1][0],hour[2][0])
done=max(hour[0][1],hour[1][1],hour[2][1])
hour_list=[0]*(done+1)

for i in range(3):                              # 구간 설정을 조심해야 할 듯
    for k in range(hour[i][0]+1,hour[i][1]+1): #(hour[i][0],hour[i][1]+1) 일때는 안되는 이유?
        hour_list[k]+=1                         #(hour[i][0]+1,hour[i][1]+1)일때 정답
# hour_list.pop(-1)
# print(hour_list)
sum_=0
sum_+=A*hour_list.count(1)
# print(hour_list.count(1))
sum_+=B*hour_list.count(2)*2
# print(hour_list.count(2))
sum_+=C*hour_list.count(3)*3
# print(hour_list.count(3))
print(sum_)
