from math import *
t=int(input())
while t>0:
    n=int(input())
    a,b=map(int,input().split())
    n=str(n)
    lst=list(n)
    d=0
    lst2=[]
    while len(lst)>0:
        c=int(lst[d])
        e=0
        if(c<len(lst)):
            for i in range(c):
                e=e*10 +int(lst[i])


            for i in range(c):
                lst.pop(0)

        else:
            for i in range(len(lst)):
                e=e*10 +int(lst[i])
            for i in range(len(lst)):
                lst.pop(0)

        lst2.append(e)

    sum=1
    for i in range(len(lst2)):
        sum=sum*lst2[i]
    ans=int(sum%(pow(10,a)+b))
    print(ans)


    t=t-1