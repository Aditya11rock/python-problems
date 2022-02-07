from numpy import *
t=int(input())
while t>0:
    n=int(input())
    lst=[int(i) for i in input().split()][:n]
    lst2=zeros((n,2),int)
    for i in range(n):
        lst2[i][0]=lst[i]
        s=bin(lst[i])
        a=s.count("1")

        lst2[i][1]=a
    for i in range(n):
        y=lst2[i][1]
        for j in range(i-1,-1,-1):
            if(lst2[j][1]>y):
                d=lst2[j+1][1]
                e=lst2[j+1][0]
                lst2[j+1][0]=lst2[j][0]
                lst2[j+1][1]=lst2[j][1]
                lst2[j][0]=e
                lst2[j][1]=y
            else:
                break
    for i in range(n):
        print(lst2[i][0],end=" ")
    print("")

    t=t-1