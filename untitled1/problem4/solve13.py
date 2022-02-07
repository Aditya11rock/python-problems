from numpy import *
t=int(input())
while t>0:
    n,m,a,b=map(int, input().split())
    lst=zeros((n,2),int)
    for i in range(n):
        c,d=map(int,input().split())
        lst[i][0]=c
        lst[i][1]=d

    lst2=[]
    for i in range(m+1):
        lst2.append(0)

    for i in range(n):
        for j in range(lst[i][0],lst[i][1]+1):
            if(lst2[j]==0):
                lst2[j]=1
    count=0

    for i in range(a,b+1):
        if(lst2[i]==0):
            count +=1

    print(count)


    t=t-1




