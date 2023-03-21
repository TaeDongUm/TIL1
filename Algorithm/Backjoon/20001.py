start=input()
problem=0
for i in range(102):
    word=input()
    if word =='고무오리 디버깅 끝':
        break
    if word=='문제':
        problem+=1
    elif word=='고무오리':
        if problem==0:
            problem+=2
        else:
            problem-=1

if problem==0:
    print('고무오리야 사랑해')
elif problem>0:
    print('힝구')
