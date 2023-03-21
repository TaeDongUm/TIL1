N =int(input())
num_list=list(map(int, input().split()))
min=1000000 # 무한대는 어떻게 짤까?
max=-1000000
if len(num_list)==1:
    min = num_list[0]
    max = num_list[0]
for i in range(N-1):
    if num_list[i] <= num_list[i+1]:
        if num_list[i] <= min:
             min=num_list[i]
    else:
        if num_list[i+1] <= min:
            min = num_list[i+1]
for i in range(N-1):
    if num_list[i] <= num_list[i+1]:
        if num_list[i+1] >=max:
             max=num_list[i+1]
    else:
        if num_list[i] >= max:
            max = num_list[i]
print(min, end=' ')
print(max, end='')

