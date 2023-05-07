n = int(input())

for a in range(0,n):
    for b in range(0,a+1):
        print('*', end='')
    for c in range(0,2*n-2*a-2):
        print(' ', end='')
    for d in range(0, a+1):
        print('*', end='')
    print('')       
for e in range(1,n):
    g = n-e
    for f in range(0,g):
        print('*', end='')
    for h in range(0,e*2):
        print(' ', end='')
    for i in range(0, g):
        print('*', end='')
    print('')
# commit test