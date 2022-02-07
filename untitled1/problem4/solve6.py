from numpy import *
n,k=map(int,input().split())
cost=0
lst1=[int(i) for i in input().split()][:n]
lst2=[int(i) for i in input().split()][:n]
a=0
h=lst1[a]
lst3=[]
while k>0 and a<n:
    h=lst1[a]
    l=a
    for i in range(a,n):
        p=lst1[i]
        q=i-a+1
        if(h<p):
            h=p
        if(h>=q and i!=(n-1)):
            pass
        elif(i==n-1):
            l=i
            break
        else:
            l = i - 1
            break
    r=l-a
    lst4=[a+1,l+1]
    lst3.append(lst4)


    cost=cost +int(r*h)
    a=l+1
    k=k-1

print(cost)
for i in lst3:
    print(*i)





