from numpy import *
n=int(input())
lst=ones((n,2),int)
for i in range(n):
    a=int(input())
    lst[i][0]=a


for i in range(n-1):
    if lst[i][0]<lst[i+1][0]:
        lst[i+1][1]=lst[i][1]+1
    elif lst[i][0]==lst[i+1][0]:
        pass

sum=0
for i in range(n):
    sum=sum + lst[i][1]


print(sum)