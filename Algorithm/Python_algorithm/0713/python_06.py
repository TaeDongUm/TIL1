# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지
# numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100] # 100
# numbers = [0, 1, 0] # 1
# numbers = [-10, -100, -30] # -10 

numbers = [-10, -100, -30]
max_num = numbers[0]  # nubmers 값이 마이너스 값을 가지게 되면 문제가 발생할 수 있으므로
for i in numbers:
   if (max_num <=i):
    max_num = i
   
        
print(max_num)
    