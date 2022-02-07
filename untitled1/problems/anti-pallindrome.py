t=int(input())
while t>0:
    n=input()
    b=len(set(n))

    if b>1:
        lst=list(n)
        lst.sort()
        for i in range(len(n)):
            print(lst[i],end="")
        print("")
    elif b==1 or b==0:
        print("-1")

    t=t-1