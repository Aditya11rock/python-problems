t=int(input())
while(t>0):
    n=int(input())
    lst=[int(i) for i in input().split()][:n]
    b=set(lst)
    if(len(b)>1):
        q=True
    else:
        q=False
    c=0
    while q:
        d=max(lst)
        e=lst.index(d)
        a=0
        for i in range(n):
            if i!=e:
                lst[i]+=1
                if(lst[i]<d)or(lst[i]>d):
                    a=a+1

        if not(a>0):
            q=False
        c=c+1

    print(c)

    t=t-1