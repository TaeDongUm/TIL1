# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# ## 추가 정보
# 아스키코드는 영문 알파벳을 사용하는 대표적인 문자 인코딩이고, 
# 이후 아스키 기반의 확장 인코딩(유니코드 등)이 등장하게 되었다.
# ### 파이썬 활용

# 특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 `ord` 이다.

# [https://docs.python.org/ko/3/library/functions.html#ord](https://docs.python.org/ko/3/library/functions.html#ord)

# ```python
# ord('a') 
# # 97
# ```

# 해당 유니코드 숫자를 문자로 반환하는 함수는 `chr`이다. 

# [https://docs.python.org/ko/3/library/functions.html#chr](https://docs.python.org/ko/3/library/functions.html#chr)

word = input()
num =0
for i in word:
    num = ord(i) -32
    i = chr(num)
    print(i, end='')

    
