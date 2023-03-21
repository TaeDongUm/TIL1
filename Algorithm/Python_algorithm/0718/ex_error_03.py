# 두 수를 Input으로 받아 합을 구하는 코드이다.
# # 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# numbers = input().split()
# print(sum(numbers))

# 원인 입력 받아 저장한 값의 type은 int가 아닌 list이며, 저장된 값은 str이다.
# 리스트 안의 값들을 int형으로 바꾸고 싶다면?
# 예: list_a = ['1', '2', '3', '4']   -> list_a = [1, 2, 3, 4] 로 바꾸고 싶을 때
# python 2. list_a = map(int, list_a)
# python 3. list_a = list(map(int, list_a))를 해주면 된다.
# 혹은 list_a = [int (i) for i in list_a]

numbers = input().split()
numbers = map(int, numbers)
numbers = list(map(int, numbers))

print(numbers, numbers[0], type(numbers), type(numbers[0]))
print(sum(numbers))