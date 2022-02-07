t=int(input())
while t>0:
    m=input()
    s=input()
    a=len(m)
    lst=[]
    for i in range(a):
        lst.append(m[i])

    lst.sort()

    b=s[0]
    e=s.count(b)
    f=m.count(b)
    c=f-e

    z=1
    p=len(s)
    while p>1:
        x=s[z]
        q=lst.index(x)
        lst.pop(q)
        z=z+1
        p=p-1
    j=lst.index(b)
    j=j+c
    y=''
    for i in range(j):
        y=y + lst[i]

    y=y + s
    for i in range(j+1,len(lst)):
        y=y + lst[i]

    print(y)
    t=t-1

