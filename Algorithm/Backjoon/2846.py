T = int(input())
b=list(map(int, input().split()))
SmallList=[]
BigList=[]
new_small=[]
for i in range(T):
    if i == T-1:
        if new_small !=[]:
            BigList.append(new_small)
            break
        elif new_small ==[]:
            break
    if b[i] < b[i+1]:
        SmallList.append(b[i])
        SmallList.append(b[i+1])
        new_small = list(set(SmallList))
    if b[i] > b[i+1]:
        if new_small !=[]:
            new_small.sort() 
            BigList.append(new_small)
            new_small=[]
            SmallList=[]
        elif new_small ==[]:
            pass
    if b[i]==b[i+1]:
        if new_small !=[]:    
            new_small.sort()   # 주의! new_small.sort()는 새로운 리스트를 반환하는 것이 아니기 때문에 none이 뜬다. 
            BigList.append(new_small) # 즉, 기존의 리스트를 사용해야 한다.
            new_small=[]
            SmallList=[]
        elif new_small ==[]:
            pass    
list_sum=0
for i in range(len(BigList)):    
    if list_sum < BigList[i][-1] - BigList[i][0]:
        list_sum = BigList[i][-1] - BigList[i][0]
print(list_sum, end='')

# list(set())이런 식으로 set을 하게 되면 정렬이 안됨. 인덱싱, 정렬을 지원하지 않음
# 참고 자료: https://ratsgo.github.io/data%20structure&algorithm/2017/10/25/hash/
# 참고 자료: https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Data%20Structure/Hash.md
# 참고 자료: https://docs.python.org/2/library/sets.html