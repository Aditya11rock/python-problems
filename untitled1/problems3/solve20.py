n=int(input())
t=input()
lst=list(t)
q=int(input())
while q>0:
    p=input()
    lst2=[int(i) for i in p.split()]
    if(lst2[0]==1):
        if(lst[lst2[1]]=='0'):
            lst[lst2[1]]='1'
    elif(lst2[0]==0):
        s=''
        for i in range(lst2[1],lst2[2]+1):
            s=s +lst[i]

        y=int(s,2)
        r=int(y%3)
        print(r)

    q=q-1