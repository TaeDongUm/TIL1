import sys
dict={
    'black':'0',
    'brown':'1',
    'red':'2',
    'orange':'3',
    'yellow':'4',
    'green':'5',
    'blue':'6',
    'violet':'7',
    'grey':'8',
    'white':'9'
}

ohm=''
for i in range(2):
    color=sys.stdin.readline().strip()
    ohm+=dict[color]
color=sys.stdin.readline().strip()
print(int(ohm)*10**(int(dict[color])))

# color = ['black', 'brown', 'red', 
# 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
# f = color.index(input())
# s = color.index(input())
# t = color.index(input())
# r = int(str(f) + str(s)) * (10 ** t)
# print(r)