t=int(input())

def jon(ls):
    s=''
    for i in range(len(ls)):
        if(lst[i]=='1'):
            s=s+"(2<<"+str(len(ls)-i-2)+") + "

    return s

def jat(x):
    s=""
    return s.join(x)

while t>0:
    n,m=map(int,input().split())
    c=n*m
    b=bin(c)
    lst=list(b)
    lst.pop(0)
    lst.pop(0)
    d=jon(lst)
    lst2=list(d)
    for i in range(len(lst2)-1,-1,-1):
        if(lst2[i]==")"):
            break
        else:
            lst2.pop()

    e=jat(lst2)
    print(e)
    t=t-1