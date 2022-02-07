t=int(input())
while t>0:
    n=int(input())
    lst=[]
    for i in range(n):
        b=input()
        if b in lst:
            pass
        else:
            lst.append(b)
    d=len(lst)
    lst.sort()
    for i in range(d):
        print(lst[i])


    t=t-1