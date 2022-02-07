t=int(input())
while t>0:
    a,b=map(int , input().split())
    lst=[int(i) for i in input().split()][:a]
    final=0
    sum2=0
    for i in range(a):
        if(lst[i]<=b):
            sum2=sum2 + lst[i]
        elif(lst[i]>b):
            if(sum2>=final):
                final=sum2
                sum2=0
    print(final)

    t=t-1