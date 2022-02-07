from numpy import *
t=int(input())
n=input()
a=n.count('#')
lst=ones((a,2),int)
for i in range(a):
    b,c=map(int,input().split())
    lst[i][0]=b
    lst[i][1]=c
d=n.count('(')
lst2=ones((d,3),int)
for i in range(d):
    b,c,h=map(int,input().split())
    lst2[i][0]=b
    lst2[i][1]=c
    lst2[i][2]=h

print('Yes')