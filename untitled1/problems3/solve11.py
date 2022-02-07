from math import *
n=int(input())
while n>0:
    t,t1,t2,v1,v2,d=map(int,input().split())
    if(t1<t and t2>=t):

        l=ceil((d/v2)*60)
        time=t + (t2-t)+l
        print(time)
    elif(t2<t and t1>=t):
        l=ceil((d/v1)*60)
        time=t +(t1-t)+l
        print(time)
    elif(t1>=t and t2>=t):
        l1=ceil((d/v1)*60)
        time1=t +(t1-t)+l1
        l2 = ceil((d / v2) * 60)
        time2 = t + (t2 - t) + l2
        if(time1<=time2):
            print(time1)
        else:
            print(time2)

    else:
        print("-1")

    n=n-1