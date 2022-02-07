t=int(input())
while t>0:
    n=input()
    lst=[]
    lst2=[]
    for i in range(len(n)):
        lst.append(n[i])
        if n[i] in lst2:
            pass
        else:
            lst2.append(n[i])

    b=len(lst2)
    if b==3:
        c=lst.count(lst2[0])
        d=lst.count(lst2[1])
        e=lst.count((lst2[2]))
        if c==d and d==e and c==e:
            print("OK")
        else:
            print("Not OK")
    else:
        print("Not OK")

    t=t-1