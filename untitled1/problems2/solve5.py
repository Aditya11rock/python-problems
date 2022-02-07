t=int(input())
while t>0:
    k,r,v=map(int,input().split())

    lst=[]
    lst.append(k)
    lst.append(r)
    lst.append(v)
    lst.sort()
    if(lst[1]<lst[2]):
        a=2*lst[1] +1
        print(a)
    elif(lst[1]==lst[2]):
        a=2*lst[1]
        print(a)

    t=t-1