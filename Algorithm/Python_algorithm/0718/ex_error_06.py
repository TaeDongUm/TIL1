# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)
# print(answer)

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# AttributeError: 'tuple' object has no attribute 'append'

# 'tuple'형 데이터는 append라는 method를 built-in method로 제공하지 않습니다.

# Python이 제공하는 기본 데이터형(Primitive Data Type)에 대한 학습이 필요하신 것 같습니다.

# 자세한 내용은 아래의 Python Document를 참고 해 주세요.

# https://docs.python.org/3/library/stdtypes.html

# 소괄호 ( )로 이루어진 튜플은 값 수정이나 삭제, 추가를 할 수 없습니다.
#  append로 값을 추가하려면 대괄호 [ ] 로 리스트를 만드시면 돼요.


