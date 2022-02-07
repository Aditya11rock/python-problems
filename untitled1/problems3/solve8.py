t=int(input())
while t>0:
    n=int(input())
    lst=[int(i) for i in input().split()][:n]

    rohan=lst[0]
    r=1
    a=n-1
    b=0
    riya=lst[n-1]
    y=1
    for i in range(1,n-1):
        if(int(rohan/2)<riya):
            r=r+1
            b=b+1
            rohan=rohan + lst[b]
        elif(riya<int(rohan/2)):
            a=a-1
            y=y+1
            riya=riya + lst[a]
        elif(riya==int(rohan/2)):
            r=r+1
            b=b+1
            rohan=rohan +lst[b]



    print(r,y)

    t=t-1