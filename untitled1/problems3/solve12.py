t=int(input())
while t>0:
    n,m=map(int,input().split())
    lst=[]
    for i in range(m):
        a,b=map(int,input().split())
        lst.append(a)
        lst.append(b)

    lst2=set(lst)
    for i in lst2:
        if(lst.count(i)>2):
            print("NO")
            break
    else:
        print("YES")


    t=t-1