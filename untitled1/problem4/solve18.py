n=int(input())
lst=[int(i) for i in input().split()][:n]
q=int(input())
while q>0:
    a,b=map(int,input().split())
    c=0
    d=b-a
    if(d>0):
        d=lst[a-1]
        for i in range(a-1,b):
            e=d & lst[i]
            if(e>0):
                d=lst[i]
            else:
                f=0
                while e<=0:
                    if(d%2==0):
                        d=d+1
                        c=c+1
                        e=d & lst[i]
                    elif lst[i]%2==0:
                        f=lst[i]+1
                        c=c+1
                        e=d & f
                if(f>lst[i]):
                    d=f
                else:
                    d=lst[i]


    print(c)

    q=q-1
