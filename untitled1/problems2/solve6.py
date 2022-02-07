t=int(input())
while t>0:
    n=input()
    a=0
    for i in range(len(n)):
        if(n[i]=="$"):
            a=i
            break
    lst=[]
    for i in range(a+1,len(n)):
        if("0"<=n[i]<="9"):
            b=int(n[i])
            lst.append(b)
        elif(n[i]==" "):
            pass
        else:
            break
    prize=lst[0]
    for i in range(1,len(lst)):
        prize=prize *10 +lst[i]

    print(prize)

    t=t-1