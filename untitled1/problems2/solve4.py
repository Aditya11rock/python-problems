t=int(input())
while t>0:
    n=int(input())
#no. of factors of natural no.= (a1+1)*(a2+1)....where a1,a2... are count of dictinct factors
    lst=[]
    a=2
    while n>1:
        if(n%a)==0:
            lst.append(a)
            n=int(n/a)
        else:
            a=a+1

    lst2=set(lst)
    sum=1
    for i in lst2:

        sum=sum *(lst.count(i)+1)
    print(sum)
    t=t-1