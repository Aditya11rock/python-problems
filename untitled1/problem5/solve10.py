t=int(input())
lst=[int(i) for i in input().split()][:t]
l=1
for i in range(0,len(lst)-1):
    lst2=[]
    lst2.append(lst[i])
    for j in range(i+1,len(lst)):
        if(lst[j]>=lst[j-1]):
            lst2.append(lst[j])
        else:
            tin=len(lst2)
            if tin>l:
                l=tin
            break
    else:
        tin = len(lst2)
        if tin > l:
            l = tin
    if(l>(len(lst)-i)):
        break


print(l)