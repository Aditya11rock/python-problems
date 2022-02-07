t=int(input())
while t>0:
    l,r,k=map(int,input().split())
    a=0
    for i in range(l,r+1):

        lst=list(str(i))
        for j in lst:
            if int(j)%k==0:
                pass
            elif int(j)%k!=0:
                break
        else:
            a=a+1
    print(a)
    t=t-1

