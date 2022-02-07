t=int(input())
while t>0:
    n=int(input())
    lst=[]
    for i in range(n):
        lst.append(int(input()))

    a=len(lst)
    lst.sort()
    for i in range(a-1,-1,-1):
        for j in range(i+1,len(lst)):
            if(lst[j]>lst[i]):
                lst.remove(lst[j])
                break
    print(len(lst))

    t=t-1