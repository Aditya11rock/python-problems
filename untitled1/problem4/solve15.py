n=int(input())
lst=[]
s=''
while n>0:
    t=input()
    l=0
    lst2=list(t)
    a=0
    for i in lst2:
        if(i=='E' or i=='S'):
            if(a>l):
                l=a
            a=0
        else:
            a +=1
    if(a>l):
        lst.append(a)
    else:
        lst.append(l)
    s=s +t




    n=n-1
d=0
e=0
for i in s:
    if (i == 'E' or i == 'S'):
        if (e>d):
            d=e
        e = 0
    else:
        e += 1
if(e>d):
    a=max(lst)
    print(a,end=" ")
    print(e)
else:
    a = max(lst)
    print(a, end=" ")
    print(d)