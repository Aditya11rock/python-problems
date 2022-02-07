from numpy import *
n=int(input())
lst=zeros((n,n),int)
for i in range(n):
    lst2=[int(i) for i in input().split()][:n]
    for j in range(n):
        lst[i][j]=lst2[j]

check1=False
d=0
for i in range(n):
    if(i==0):
        for j in range(n):
            if(lst[i][j]==1):
                d=i
                break
        else:
            break
    else:
        for j in range(d-1,d+2):
            if(lst[i][j]==1):
                d=i
                break
        else:
            break
else:
    check1=True

check2=False
d=0
for i in range(n):
    if(i==0):
        for j in range(n):
            if(lst[j][i]==2):
                d=i
                break
        else:
            break
    else:
        for j in range(d-1,d+2):
            if(lst[j][i]==1):
                d=i
                break
        else:
            break
else:
    check2=True

if(check1 and check2):
    print("AMBIGUOUS")
elif(check1):
    print("1")
elif(check2):
    print("2")
else:
    print("0")