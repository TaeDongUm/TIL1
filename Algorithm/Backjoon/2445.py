n = int(input())

for a in range(0,n):
    for c in range(0,a+1):
        print('*', end='')
    for c in range(0,2*n-2*a-2):
        print(' ', end='')
    for c in range(0, a+1):
        print('*', end='')
    print('')       
for b in range(1,n):
    d = n-b
    for c in range(0,d):
        print('*', end='')
    for c in range(0,b*2):
        print(' ', end='')
    for c in range(0, d):
        print('*', end='')
    print('')
# commit test