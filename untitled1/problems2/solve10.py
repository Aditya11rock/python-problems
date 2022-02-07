from numpy import *
t=int(input())
while t>0:
    n,a,b,c=map(int,input().split())
    lst=zeros((n,2),int)
    for i in range(n):
        e,f=map(int,input().split())
        lst[i][0]=e
        lst[i][1]=f
    p1=lst[0][0]

    for i in range(1,n):
        if lst[i][0]<p1:
            p1=lst[i][0]
    p2=lst[0][1]
    for i in range(1,n):
        if lst[i][1]>p2:
            p2=lst[i][1]
    lst2=zeros(((p2-p1+1),2),int)
    for i in range(p2-p1+1):
        lst2[i][0]=p1
        for j in range(n):
            if(lst[j][0]<=p1<=lst[j][1]):
                lst2[i][1]+=1
        p1+=1
    p3=lst2[0][0]
    l=lst2[0][1]
    for i in range(1,len(lst2)):
        if lst2[i][1]>=l:
            l=lst2[i][1]
            p3=lst2[i][0]
    ans=0

    for i in range(n):
        if(lst[i][0]<=p3<=lst[i][1]):
            ans=ans + b
        elif(lst[i][1]<p3):
            ans=ans +c
        else:
            ans=ans + a
    print(ans)

    t=t-1