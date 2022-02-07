t=int(input())
while t>0:
    n=int(input())
    lst=[int(i) for i in input().split()]
    a=0
    lst.sort()
    while len(lst)!=0:
        x=lst.pop()
        a=a+1
        if (x-1) in lst:

            lst.pop()
    print(a)
    t=t-1

