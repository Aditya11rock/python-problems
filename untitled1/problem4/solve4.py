t=int(input())
while t>0:
    n=int(input())
    lst=[int(i) for i in input().split()][:n]
    total=int(input())
    sum=0
    val=0
    while sum<total:
        for i in range(len(lst)):
            sum=sum + lst[i]
            if(sum<total):
                val=i+1
            elif(sum>=total):
                val=i+1
                break
    print(val)




    t=t-1