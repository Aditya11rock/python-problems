t=int(input())
while t>0:
    n=input()
    lst=[int(i) for i in n.split()]
    l=lst.pop(0)
    lst.sort()
    lst2=[]
    for i in range(int(l/2)):
        b=lst[i]+lst[l-i-1]
        lst2.append(b)

    c=max(lst2)
    d=min(lst2)

    print(c-d)


    t=t-1