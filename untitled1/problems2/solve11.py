n=int(input())
lst=[int(i) for i in input().split()][:n]
lst2=[]
for i in range(n-1):
    for j in range(n-1,i,-1):
        if(lst[i]==lst[j]):
            a=j-i+1
            lst2.append(a)
            break

ans=max(lst2)
print(ans)