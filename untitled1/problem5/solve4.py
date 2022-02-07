from math import *
t=int(input())
while t>0:
    n=int(input())
    lst=[]
    for i in range(n):
        p=input()
        lst.append(p)
    a=0
    b=0
    for i in range(n):
        c=lst[i]
        lst1=list(c)
        d=0
        for j in range(n):
            if(lst1[j]=='*'):
                a=i+1
                b=j+1
                d=1
                break

        if d==1:
            break

    e=ceil(n/2)
    f=abs(e-a)+abs(e-b)
    print(f)


    t=t-1