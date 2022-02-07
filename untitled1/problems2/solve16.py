#cyclic rotation of string
t=int(input())
while t>0:
    n=input()
    lst=list(n)
    lst2=[]
    a=1
    p=1
    while a<=len(n):
        c=lst[len(n)-1]
        d=lst[0]
        for i in range(len(lst)-1):
            e=lst[i+1]
            lst[i+1]=d
            d=e
        lst[0]=c
        if lst!=list(n):
            s=''
            for i in lst:
                s=s +i
            if s in lst2:
                pass
            else:
                lst2.append(s)
                p +=1
        a=a+1

    print(p)


    t=t-1