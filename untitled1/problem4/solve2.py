from math import *
t=int(input())
while t>0:
    n=int(input())
    count=n
    a=2
    p=pow(2,2)
    while n/p>=1:
        while p<=n:
            count=count +1
            p=p+a
        a=a+1
        p=pow(a,2)
    print(count)

    t=t-1