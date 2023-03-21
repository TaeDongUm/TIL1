word = input().upper() 
print(word, type(word)) #MISSISSIPI <class 'str'>
capital_list = list(set(word))    #set있는 경우 중복제거['M', 'P', 'I', 'S'] <class 'list'>  set 없는 경우: ['M', 'I', 'S', 'S', 'I', 'S', 'I', 'P', 'I'] <class 'list'>
cnt = []

for i in capital_list:   #['I', 'M', 'S', 'P']
    count = word.count(i)
    cnt.append(count)    #[4, 1, 4, 1]

if cnt.count(max(cnt)) >= 2: #count 숫자 최대값이 중복되면  
    print('?')

else:
    # print(capital_list[(cnt.index(max(cnt)))])
    print(max(cnt))