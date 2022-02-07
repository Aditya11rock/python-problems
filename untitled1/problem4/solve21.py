t=int(input())
while t>0:
    a,n=map(int,input().split())
    lst=[int(i) for i in input().split()][:n]
    b=0
    for i in range(len(lst)):
        if(lst[i]==0):
            a=a -1
            if(a==0 and i!=len(lst)-1):
                b=i+1
                break
        else:
            a=a+2
    else:
        print("Yes",end=" ")
        print(a)

    if(b!=0):
        print("No",end=" ")
        print(b)

    t=t-1