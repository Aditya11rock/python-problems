t=int(input())
while t>0:
    n=int(input())
    lst=[]
    for i in range(n):
        a=input()
        lst.append(a)
    sleep=input()
    lst2=list(sleep)
    lst2.sort()
    lst3=[]
    for i in range(n):
        for j in lst[i]:
            if j in lst2:
                pass
            else:
                break
        else:
            for j in lst[i]:
                lst3.append(j)
            lst3.sort()
            if(lst3==lst2):
                print("YES")
                break

    else:
        print("NO")

    t=t-1
