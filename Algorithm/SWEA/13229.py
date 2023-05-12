T = int(input())
for i in range(T):
    DAY=['MON','TUE','WED','THU','FRI','SAT','SUN']
    TODAY = input()
    if TODAY == 'SUN':
        print(f'#{i+1} 7')
    else:
        count = DAY.index(TODAY)
        count = 6- count
        print(f'#{i+1} {count}')