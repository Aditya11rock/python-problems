from numpy import *

t=int(input())
while t>0:
    n,m=map(int,input().split())
    p=0
    if n>=m:
        lst = zeros((n, n), int)
        p=n
    else:
        lst = zeros((m, m), int)
        p=m


    for i in range(m):
        a,b=map(int,input().split())
        lst[a-1][b-1]=1
        lst[b-1][a-1]=1
    lst2=[0]
    lst3=[0]
    a=0


    c=0
    while len(lst2)>0:
        a=lst2.pop(0)
        for i in range(p):
            if lst[a][i]==1:
                if i in lst3:
                    pass
                else:
                    lst3.append(i)
                    lst2.append(i)
                if (i+1)==n:
                    print(a+1)
                    c=1
                    break

        if c==1:
            break



    t=t-1