t=int(input())

def jon(p):
    e=""
    return e.join(p)

while t>0:
    n=int(input())
    lst=[str(i) for i in input().split(" ")][:n]
    lst2=[]
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            lst3=list(lst[i])
            lst4=list(lst[j])
            a=lst3.pop(0)
            b=lst4.pop(0)
            lst3.insert(0,b)
            lst4.insert(0,a)
            c=jon(lst3)
            d=jon(lst4)
            if c in lst:
                pass
            else:
                if c in lst2:
                    pass
                else:
                    lst2.append(c)
                    lst2.append(d)

    print(len(lst2))
    t=t-1