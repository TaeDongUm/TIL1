# 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

# * 사각형 넓이 : 가로 * 세로
# * 사각형 둘레 : (가로 + 세로) * 2

width = int(input())
vertical = int(input())

def rectangle(a,b):
    area = a*b
    result1 = area
    round = 2*a + 2*b
    result2 = round
    print('넓이 = %d, 둘레 = %d' %(result1, result2))

rectangle(width, vertical)
