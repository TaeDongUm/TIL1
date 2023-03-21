# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    new_list=[]
    value=0
    for i in range(len(numbers)-1):
        value += 1 
        for j in range(len(numbers)-(i+1)):
            new_num = numbers[i] + numbers[j+value]  
            new_list.append(new_num)
        
    new_list1 = sorted(set(new_list)) # 정렬을 돌리는 건 시간을 좀 잡아먹는 과정이어서 반복문 안에서 돌리기보다 밖에서 돌리는 것이 낫다
    return new_list1
# input값이 리스트인 경우 number = input([2,1,3,4,10])은 어떤 값을 받는건가?
# 리스트가 아니라 str임. [도 문자열로 인식
# 그냥 리스트를 입력으로 받지 않고 고정시켜서 품
print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))
