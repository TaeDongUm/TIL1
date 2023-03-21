N = int(input())
sequence=list(map(int, input().split()))
cnt=0
check=sorted(set(sequence))
for i in range(len(check)):
    cnt +=sequence.count(check[i])-1
print(cnt)