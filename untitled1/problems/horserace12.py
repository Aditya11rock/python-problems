t=int(input())
while t>0:
    n=int(input())
    lst=[int(i) for i in input().split()][:n]
    lst.sort()
    min=lst[1]-lst[0]
    for i in range(1,n-1):
        a=lst[i+1]-lst[i]
        if(a<min):
            min=a

    print(min)
    t=t-1