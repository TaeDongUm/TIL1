from collections import deque
import copy

N = int(input())
num_list=[]
new_list1=[]
for i in range(1,N+1):
    num_list.append(i)
new_list=deque(num_list)
for i in copy.deepcopy(new_list):    #RuntimeError: deque mutated during iteration 에러, 그래서 list 넣었음
    new_list1.append(new_list[0])  
    new_list.popleft()
    if len(new_list) ==0:        
        break      
    new_list.append(new_list[0])  
    new_list.popleft()            
    if len(new_list) ==1:
        new_list1.append(new_list[0])
        break
print(*new_list1,end='')

#RuntimeError: deque mutated during iteration 에러, 그래서 list 넣었음
# 이렇게 했더니 백준사이트에서는 런타임 에러 (IndexError)
# 그래서 import copy했더니 똑같은 에러 뜸
# Indexerror 뜨는 이유가 아마 input으로 1부터 넣을 수 있는데 13~14줄이 없을 경우
# [] 상태에서 new_list.append(new_list[0])를 진행하게 돼서 그런 것 같다
# 그래서 13~14줄을 추가했고 백준풀이로 맞았다.