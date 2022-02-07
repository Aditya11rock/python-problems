from math import *
t=int(input())
while t>0:
    h,p=map(int , input().split())
    a=ceil(h/9)
    b=ceil(p/9)
    if a<b:
        print("0 ",a)
    elif b<=a:
        print("1 ",b)

    t=t-1

