T = int(input())
Clock=[]
for i in range(T):
    Clock.append(list(map(int,input().split())))
for i in range(len(Clock)):
    hour = Clock[i][0] + Clock[i][2]
    minute = Clock[i][1] + Clock[i][3]
    if minute >= 60:
        minute = minute - 60
        hour +=1
    if hour > 12:
        hour = hour - 12
        if hour > 12:
            hour = hour
    print(f'#{i+1} {hour} {minute}') 

