from math import *
t=int(input())
while t>0:
    a,b,c,d=map(int,input().split())
    lst=[]
    lst.append(a)
    lst.append(b)
    for i in range(2,c):
        p=int((lst[i-1]+lst[i-2])%d)
        lst.append(p)

    q=set(lst)
    lst2=[]
    for i in q:

        r=lst.count(i)
        lst2.append(r)

    force=0
    for i in lst2:
        force=force + pow(i,2)
    force=int(force)
    print(force)

    t=t-1