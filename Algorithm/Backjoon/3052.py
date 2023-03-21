number=[]
remainder=[]
for i in range(10):
    num_input = int(input())
    number.append(num_input)
for i in range(len(number)):
    num1 = number[i] % 42
    remainder.append(num1)
print(len(set(remainder)), end='')
