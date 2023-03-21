K = int(input())
num_list=[]
for i in range(K):
    number =int(input())
    num_list.append(number)
    if number == 0:
        num_list.pop()
        num_list.pop()
        i = i-2
        K = K-2
print(sum(num_list))
# [0,1,2,3,4] 10
# [1,3,5,4,0,0,7,0,0,6]
# [1,3,4,]list
# [0,1,2]i
