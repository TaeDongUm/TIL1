# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# words = list(map(int, input().split()))
# print(words)

words = list(map(str, input().split()))
print(words)

# ValueError: invalid literal for int() with base 10: 'word'
# 입력 받은 값은 int(string 값임)가 아니기 때문에 int로 받을 수 없음


