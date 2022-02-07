n=int(input())
lst=[int(i) for i in input().split()][:n]
for i in range(n-1):
    while lst[i]>0:
        lst[i]-=1
        lst[i+1]-=1
        if(lst[i+1]==0 and lst[i]!=0):
            break

m=max(lst)
if(m>0):
    print("NO")
else:
    print("YES")
