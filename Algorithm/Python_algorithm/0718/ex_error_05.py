# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number = 22020718
# print(len(number))

number = 22020718
number = str(number)
print(len(number))

# TypeError: object of type 'int' has no len()
# len이란 함수는 문자열의 길이를 변환하는 함수이므로 int형은 반환 못한다.
