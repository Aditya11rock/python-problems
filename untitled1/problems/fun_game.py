n=int(input())
lst=[int(i) for i in input().split()][:n]

a=0
b=n-1
e=True
while e:
    if lst[a]>lst[b]:
        print(1,end=' ')
        c=lst.pop(b)
        b=b-1
    elif lst[a]<lst[b]:
        print(2,end=' ')
        c=lst.pop(a)
        b=b-1
    else:
        print(0,end=" ")
        if len(lst)>1:
            c=lst.pop(a)
            d=lst.pop(b)
            b=b-2
        else:
            c=lst.pop(b)
            b=b-1

    if len(lst)==0:
        e=False

print("")