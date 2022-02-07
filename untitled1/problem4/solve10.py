t=int(input())
lst=[int(i) for i in input().split()][:t]
lst.sort()
max=0
for i in range(t-1,-1,-1):
    a=0
    for j in range(2,lst[i]):
        if(lst[i]%i==0):
            break

    else:
        max=lst[i]
        a +=1
    if(a==1):
        break

min=0
for i in range(t):
    a = 0
    for j in range(2, lst[i]):
        if (lst[i] % i == 0):
            break

    else:
        min = lst[i]
        a += 1
    if (a == 1):
        break

ans=abs(max-min)
print(ans)