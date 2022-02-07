t=int(input())
while t>0:
    n,k=map(int,input().split())

    lst=[int(i) for i in input().split()][:n]
    for i in range(n-1):
        d=bin(lst[i])
        for j in range(i+1,n):
            e=bin(lst[j])
            if(d.count('1')<e.count('1')):
                f=lst[i]
                lst[i]=lst[j]
                lst[j]=f

    sum=0
    for i in range(k):
        z=bin(lst[i])
        sum=sum + z.count('1')

    print(sum)

    t=t-1