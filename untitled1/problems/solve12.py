from math import *
t=int(input())
while t>0:
    l,b,h=map(int,input().split())
    vol=l*b*h
    a=1
    for i in range(1,int(vol/2)):
        if (vol%(pow(i,3))==0):
            a=i
    no=int(vol/pow(a,3))
    print(a,end=" ")
    print(no)

    t=t-1