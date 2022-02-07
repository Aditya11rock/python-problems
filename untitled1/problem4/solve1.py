t=int(input())
while t>0:
    n=int(input())
    l=1
    b=1
    p=2*l +2*b
    a=l*b
    while p<n:
        if(l<=b):
            l=l+1
            p=2*l + 2*b
            if(p<=n):
                a=int(l*b)
            elif(p>n):
                break
        elif(b<l):
            b=b+1
            p = 2 * l + 2 * b
            if (p <= n):
                a = int(l * b)
            elif (p > n):
                break
    print(a)
    t=t-1