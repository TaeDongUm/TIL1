Word=input()
List=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
for i in List:
    for k in range(len(Word)):
        if i in Word:
            Word=Word.replace(i,'0',1)
            cnt+=1
        else:
            break
for i in Word:
    if i !='0':
        cnt +=1
print(cnt,end='')
