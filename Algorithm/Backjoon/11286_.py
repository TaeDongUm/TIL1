import heapq
T=int(input())
A=[]
abs_list=[]
for i in range(T):
    x = int(input())
    if x !=0:
        A.append(x)
    else:
        if A==[]:
            print(0)
        else:
            A=sorted(A,key=lambda x:(abs(x)))
            if A[0]>0:
                for i in range(len(A)):
                    if abs(A[i])==A[0] and A[i]<0:
                        print(A[i])
                        del A[i]
                        break
                    elif abs(A[0]) < abs(A[i]):
                        print(A[0])
                        del A[0]
                        break
            elif A[0]<0:
                print(A[0])
                del A[0]
                

            

