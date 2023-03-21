# def solution(absolutes, signs):
#     sum_=0
#     for i in range(len(absolutes)):
#         if signs[i] == true:
#             absolutes[i] = absolutes[i]*true
#         if signs[i] == false:
#             absolutes[i] = absolutes[i]*false
#         sum_ += absolutes[i]
#     return sum_ 
# true=1
# false=-1
# print(solution([4,7,12], [true, false, true]))
# print(solution([1,2,3], [false, false, true]))

# 여전히 어떻게 입력을 리스트로 받는지 이해를 못했음

def solution(absolutes, signs):
    sum_=0
    true=1
    false=-1
    for i in range(len(absolutes)):
        if signs[i] == true:
            plus=1
            absolutes[i] = absolutes[i]*plus
        if signs[i] == false:
            minus=-1
            absolutes[i] = absolutes[i]*minus
        sum_ += absolutes[i]
    return sum_ 
# 다른 분들 코드 참고: https://school.programmers.co.kr/learn/courses/30/lessons/76501/solution_groups?language=python3
# 파이썬에서 True, False를 사용할 때는 반드시 앞문자는 대문자여야 함
# 하지만 프로그래머스에서 위 코드를 돌리면 맞다고 뜸. 여전히 프로그래머스가 어떻게 코드를 돌리는지 이해 못했음
# 참고: https://wikidocs.net/17
