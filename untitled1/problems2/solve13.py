from math import *
n,q=map(int,input().split())
lst=[int(i) for i in input().split()][:n]
while q>0:
    n=input()
    lst2=[]
    for i in n:
        if(i!=' '):
            p=int(i)
            lst2.append(p)
    if(lst2[0]==1):
        for i in range((lst2[1])-1,(lst2[2])):
            lst[i]=(lst2[3])

    elif(lst2[0]==2):
        for i in range(lst2[1]-1,lst2[2]):
            f=gcd(lst[i],lst2[3])
            lst[i]=f

    elif(lst2[0]==3):
        max=0
        for i in range(lst2[1]-1,lst2[2]):
            if(lst[i]>max):
                max=lst[i]
        print(max)

    else:
        sum=0
        for i in range(lst2[1]-1,lst2[2]):
            sum = sum +lst[i]
        print(sum)


    q=q-1