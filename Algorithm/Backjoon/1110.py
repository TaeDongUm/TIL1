num_list=[]
Num1=[]
N = int(input())
while 1:
    n1 = N%10
    num_list.append(n1)
    N//=10
    if N==0:
        break
num_list.reverse()
if len(num_list) ==1:
    num_list.insert(0,0)
Num1.append(num_list[0])  # 그냥 Num1 = num_list로 하니 num_list가 바뀌면 Num1도 바뀜
Num1.append(num_list[1])  # 그래서, 밑에   if Num1==num_list:가 항상 참이 되게 됨. 각각의 리스트를 독립적으로 만들려면?
cnt=0
while 1:
    sum_=[]
    Sum_ =0
    for i in range(len(num_list)):
        Sum_+=num_list[i] 
    while 1:
        n1 = Sum_%10
        sum_.append(n1)
        Sum_//=10
        if Sum_==0:
            break
    sum_.reverse()
    num_list[0]=num_list[-1]
    num_list[1]=sum_[-1]
    cnt+=1
    if Num1==num_list:
        break
print(cnt)