n=int(input())
lst=[int(i) for i in input().split()][:n]
q=int(input())
while q>0:
    t=input()
    lst2=[int(i) for i in t.split()]
    if lst2[0]==1:
        for i in range(lst2[1]-1,lst2[2]):
            lst[i]=lst[i] + lst2[3]

    elif lst2[0]==2:
        for i in range(lst2[1]-1,lst2[2]):
            lst[i]=lst[i] * lst2[3]

    else:
        a=-1
        b=-1
        for i in range(n):
            if lst[i]==lst2[1]:
                a=i
                break
        for i in range(n-1,-1,-1):
            if lst[i]==lst2[1]:
                b=i
                break
        if a!=-1 and b!=-1:
            c=b-a + 1
            print(c)
        else:
            print(-1)

    q=q-1