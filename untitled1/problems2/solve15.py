t=int(input())
while t>0:
    n,x=map(int,input().split())
    lst=[]
    for i in range(n):
        a=int(input())
        lst.append(a)
    for i in range(n-1):
        b=0
        sum=0
        for j in range(i,n):
            sum=sum +lst[j]
            if(sum<x):
                pass
            elif(sum==x):
                print("YES")
                b +=1
                break
            elif(sum>x):
                break

        if(b==1):
            break
    else:
        print("NO")



    t=t-1