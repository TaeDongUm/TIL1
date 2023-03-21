# T = [0,1,2,3,4,5]
# num =[]
# for i in range(len(T)):
#      num.append(i)
# if T == num:
#     print('same')

T = [0,1,2,3,4,5]
num =[5,4,3,2,1,0]
num=list(set(num))
if T == num:
    print('same')

