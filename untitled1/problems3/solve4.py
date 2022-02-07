from numpy import *
n=int(input())
lst=[int(i) for i in input().split()][:n]
lst.sort()
lst2=zeros((n,1),int)
a=0
b=n-1
for i in range(n):
    if(i%2==0):
        lst2[a][0]=lst[n-i-1]
        a=a+1
    else:
        lst2[b][0]=lst[n-i-1]
        b=b-1

max=0
for i in range(n-1):
    r=abs(lst2[i][0]-lst2[i+1][0])
    if(r>max):
        max=r
d=abs(lst2[n-1][0]-lst2[0][0])
if(d>max):
    max=d

print(max)