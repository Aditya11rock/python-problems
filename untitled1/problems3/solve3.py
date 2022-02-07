t=int(input())
while t>0:
    n,total=map(int,input().split())
    lst=[]
    for i in range(n):
        a=int(input())
        lst.append(a)
    for i in range(n):
        sum=0
        b=0
        for i in range(i,n):
            sum=sum+lst[i]
            if(sum<total):
                pass
            elif(sum==total):
                print("YES")
                b=b+1
                break
            elif(sum>total):
                break
        if(b==1):
            break
    else:
        print("NO")


    t=t-1