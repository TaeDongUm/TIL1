# A=[]
# print(A[0])

# 리스트에 아무것도 없는데 A[0]을 출력하라고 하면 index 오류가 뜬다.

A=[-2,2,1,-1,1,-1]
A=sorted(A, key=abs)
print(abs((A[1])))