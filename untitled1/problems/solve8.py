t=int(input())
def fact(x):
    if x==1 or x==0:
        return 1
    else:
        return x*fact(x-1)
while t>0:
    n=int(input())
    s=(fact(n))
    lst=[]

    d=0
    while s%10==0:
        d=d+1
        s=int(s/10)


    print(d)


    t=t-1