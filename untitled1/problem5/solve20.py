def por(x):
    for i in range(2,len(x)):
        print(x[i],end="")
    print("")
t=int(input())

while t>0:
    n=input()
    lst=list(n)
    p=0
    ba=True
    while ba:
        lst2=list(bin(p))
        q=2
        for i in lst:
            if i==lst2[q]:
                q=q+1
                if q>=len(lst2):
                    break
        else:
            por(lst2)
            ba=False

        p=p+1

    t=t-1