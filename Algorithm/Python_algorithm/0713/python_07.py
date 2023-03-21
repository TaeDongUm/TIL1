# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사 용 금지
# numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100] # -60
#numbers = [0, 1, 0] # 0
#numbers = [-10, -100, -30] # -100

numbers = [-10, -100, -30]
min_num = numbers[0]  # nubmers 값이 마이너스 값을 가지게 되면 문제가 발생할 수 있으므로
for i in numbers:
   if (min_num >=i):
    min_num = i
   
        
print(min_num)