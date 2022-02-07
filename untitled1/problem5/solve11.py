l=input()
q=int(input())
lst=list(l)
p=0
cp=""
lst2=[]
for i in range(len(lst)):
    if lst[i].isdigit() and i!=(len(lst)-1):
        p=p*10 +int(lst[i])
    elif lst[i].isdigit() and i==(len(lst)-1):
        p = p * 10 + int(lst[i])
        for j in range(p):
            lst2.append(cp)
        cp = lst[i]

    else:

        for j in range(p):
            lst2.append(cp)
        p=0
        cp=lst[i]

lst2.sort()

while q>0:
    a=int(input())
    if(a>(len(lst2))):
        print("-1")
    else:
        print(lst2[a-1])
    q=q-1