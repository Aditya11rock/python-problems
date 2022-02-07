t=int(input())
def rot(x):
    s=''
    return s.join(x)
while t>0:
    n,m=map(int,input().split())
    a=str(n)
    b=str(m)
    lst=list(a)
    lst2=list(b)
    for i in range(len(lst)-1,-1,-1):
        if(lst[i]=='0'):
            lst.pop(i)
        else:
            break
    for i in range(len(lst2)-1,-1,-1):
        if(lst2[i]=='0'):
            lst2.pop(i)
        else:
            break
    lst.reverse()
    c=rot(lst)
    lst2.reverse()
    d=rot(lst2)
    e=int(c)+int(d)
    e=str(e)
    lst3=list(e)
    for i in range(len(lst3)-1,-1,-1):
        if(lst3[i]=='0'):
            lst3.pop(i)
        else:
            break
    lst3.reverse()
    w=rot(lst3)
    print(w)


    t=t-1