n=int(input())
lst=[]
t=n
while t>0:
    a=input()

    lst.append(a)

    t=t-1
for i in range(n-1):
    b=lst[i]
    c=len(b)
    d=''
    for j in range(c-1,-1,-1):
        d=d+b[j]

    for k in range(i+1,n):
        if lst[k]==d:
            print(c,end=" ")
            print(d[int(c/2)])
            break



