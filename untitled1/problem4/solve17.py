
n=int(input())
lst=[]
while n>0:
    t=input()
    lst2=[str(i) for i in t.split()]
    for i in lst2:
        if i.isdigit():
            if t[0]=='G':
                a=int(i)
                lst.append(a)
                lst.append(a)
            else:
                a=int(i)
                lst.append(a)

    n=n-1

s=set(lst)
a=0
b=0
for i in s:
    d=lst.count(i)
    if(d>=a):
        a=d
        b=i

if(b==19 or b==20):
    print("Date")
else:
    print("No Date")