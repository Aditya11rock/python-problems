t=int(input())
while t>0:
    a,b,m=map(int,input().split())

    while a<b:
        if(a%m==0):
            break

        a=a+1
    while b>a:
        if(b%m==0):
            break
        b=b-1

    if(b-a>m):
        c = int((b - a) / m) + 1
        print(c)
    else:
        d=0
        for i in range(a,b+1):
            if(i%m==0):
                d=d+1
        print(d)

    t=t-1