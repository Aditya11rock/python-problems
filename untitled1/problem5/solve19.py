import numpy as np
t=int(input())
while(t>0):
    n=int(input())
    lst=[int(i) for i in input().split()][:n]
    lst2=np.ones((n,1),int)
    for i in range(n):
        lst2[i][0]=lst[i]

    ans=1
    i=0
    while i<n-1:
        slp=float(lst2[i+1][0]-lst2[i][0])
        a=0

        for j in range(i+2,n):
            p=float((lst2[j][0]-lst2[i][0])/(j-i))
            if p>=slp:
                slp=p
                a=j

        if((a-i)>ans):
            ans=a-i

        if a>0:
            i=a
        else:
            i=i+1


    print(ans)



    t=t-1

