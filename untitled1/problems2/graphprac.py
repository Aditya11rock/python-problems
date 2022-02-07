from numpy import *
n=int(input("enter no. of nodes : "))
m=int(input("enter no. of edges : "))
lst=zeros((n,n),int)
for i in range(m):
    a,b=map(int,input().split())
    lst[a-1][b-1]=1
    lst[b-1][a-1]=1

lst2=[]
lst2.append(0)
lst3=[]
lst3.append(0)
while len(lst2)>0:
    a=lst2.pop(0)
    for i in range(n):
        if(lst[a][i]==1):
            if(i in lst3):
                pass
            else:
                lst3.append(i)
                lst2.append(i)
                print("their is connection bet " + str(a + 1) + " and " + str(i + 1) + " not visited")