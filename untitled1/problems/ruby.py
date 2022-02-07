t=int(input())
while t>0:
    s=input()
    a=s.count("r")
    b=s.count("u")
    c=s.count("b")
    d=s.count("y")
    n=a;
    if(a<n):
        n=a
    if(b<n):
        n=b
    if(c<n):
        n=c
    if(d<n):
        n=d
    print(n)

    t=t-1
