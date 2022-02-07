from math import *

t=int(input())
while t>0:
    l,r=map(int, input().split())
    a=l
    b=0
    while a<=r:
        d=a
        c=0
        f=ceil(d/2)

        for i in range(1,f+1):
            if d%i==0:
                c=c+1

        if d!=1:
            c=c+1

        if (c%2)!=0:
            b=b+1


        a=a+1

    print(b)

    t=t-1