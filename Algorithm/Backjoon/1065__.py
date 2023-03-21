## 한수에 대한 문제 이해도 확인하기
# 모르면 사이트에 찾아보기

N = int(input())
cnt=0
for i in range(1,N+1):
    Number_list=[]
    while 1:
        n1 = i%10
        Number_list.append(n1)
        i=i//10
        if i ==0:
            break
    diff=[]
    if len(Number_list) ==1:
        cnt+=1
        continue
    for j in range(len(Number_list)-1):
        diff.append(Number_list[j] - Number_list[j+1])
    if min(diff) == max(diff):
        cnt+=1
print(cnt)
