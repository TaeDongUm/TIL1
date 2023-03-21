import sys
sys.stdin=open("input/2857.txt")
check=0
for i in range(5):
    name=input()
    if 'FBI' in name:
        print(i+1, end=' ')
        check=1
if check ==0:
    print("HE GOT AWAY!")

# for-else 문은 for 문이 break로 빠져나오냐 안나오냐에 따라 else문이 수행되고 안됨. break로 빠져나오면 else문 수행 안함 