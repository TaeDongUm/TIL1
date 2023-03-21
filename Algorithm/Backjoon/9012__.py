import sys
sys.stdin=open("input/9012.txt",'r')

# T = int(input())
# PS=[]
# for i in range(T):
#     PS.append(input())
# ForBreak=False
# j=0
# for i in range(len(PS)):
#     if (len(PS[i])%2==0) and (PS[i].count('(')%2 == PS[i].count(')')%2 ):
#         while 1:
#             if j == len(PS[i]):
#                 print("YES")
#                 ForBreak=True
#                 break
#             if PS[i][0]=='(':                      
#                 if PS[i][j+1] ==')':  
#                     PS[i] = ''.join(PS[i][x] for x in range(len(PS[i])) if x != j+1)
#                     PS[i] = ''.join(PS[i][x] for x in range(len(PS[i])) if x != 0)
#                     j=0
#                     continue
#                 if len(PS[i])-2 <=j:
#                     print("NO")
#                     ForBreak=True
#                     break
#                 j+=1
#                 continue
#             else:
#                 print("NO") 
#                 break   
#         # for j in range(len(PS[i])):
#         #     if j == len(PS[i]):
#         #         break
#         #     if PS[i][j+1] ==')':
#         #         PS[i] = ''.join(PS[i][x] for x in range(len(PS[i])) if x != j+1)
#         #         PS[i] = ''.join(PS[i][x] for x in range(len(PS[i])) if x != 0)
#         #         j=-1
#         if ForBreak ==True:
#             continue
#         if len(PS[i])>0:
#             print("NO")
#             break
#         else:
#             print("YES")
#             break

#     else:
#         print("NO")
#         continue


# T = int(input())
# PS=[]
# for i in range(T):
#     PS.append(input())
# ForBreak=False
# j=0
# for i in range(len(PS)):
#     if (len(PS[i])%2==0) and (PS[i].count('(')%2 == PS[i].count(')')%2 ):
#         while 1:
#             if j == len(PS[i]):
#                 print("YES")
#                 ForBreak=True
#                 break
#             if PS[i][0]=='(':                      
#                 if PS[i][j+1] ==')':  
#                     PS[i] = ''.join(PS[i][x] for x in range(len(PS[i])) if x != j+1)
#                     PS[i] = ''.join(PS[i][x] for x in range(len(PS[i])) if x != 0)
#                     j=0
#                     continue
#                 if len(PS[i])-2 <=j:
#                     print("NO")
#                     ForBreak=True
#                     break
#                 j+=1
#                 continue
#             else:
#                 print("NO") 
#                 break   
#         if ForBreak ==True:
#             continue
#         if len(PS[i])>0:
#             print("NO")
#             break
#         else:
#             print("YES")
#             break

#     else:
#         print("NO")
#         continue
     
               
      
        



# ForBreak=False
# for j in PS:
#     if len(j)%2==0:
#         if j.count('(')%2 !=0: # 짝수냐 홀수냐 (홀수여야 함)
#             for k in range(len(j)):
#                 if j[0]=='(':
#                     if j[k]==')':
#                         j.pop(0)
#                         j.pop(k)
#                     else:
#                         print("NO")
#                         ForBreak=True
#                         break
#                 else:
#                     print("NO")
#                     ForBreak=True
#                     break
#             if ForBreak ==True:
#                 break                
#             if len(j)!=0:
#                 print("No")    

#             print("YES")
            
#         else:
#             print("NO")
            
#     else:
#         print("NO")






T = int(input())
PS=[]
for i in range(T):
    PS.append(input())
for testcase in range(len(PS)):
    N=1
    while N <25:
        test=PS[testcase].replace("()", "")
        N+=1
        if test !='':
            PS[testcase]=test
        if test == '':
            break
    if len(test) !=0:
        print(test)
        print("NO")
    else:
        print("YES")
