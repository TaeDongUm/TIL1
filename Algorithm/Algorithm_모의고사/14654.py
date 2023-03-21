import sys
sys.stdin=open("예제입력2.txt",'r')
T =int(input())
for i in range(T):
    Card_num=input()
    Card_num2 = Card_num.replace('-','')
    for j in range(len(Card_num2)):
        if Card_num2[0] == '3' or Card_num2[0] == '4' or Card_num2[0] == '5' or Card_num2[0] == '6' or Card_num2[0] == '9':
            if len(Card_num2) ==16:
                print(f'#{i+1} {1}')
                break
            if len(Card_num2) !=16:
                print(f'#{i+1} {0}')
                break
        else:
            print(f'#{i+1} {0}')
            break
