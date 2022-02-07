n=int(input())
lst=[int(i) for i in input().split()][:n]
a=1
while a<=(n-1):
    lst1=[]
    k=lst[a]
    for i in range(a-1,-1,-1):
        if lst[i]>=k:
            lst1.append(i)

    for i in range(len(lst1)):
        lst[lst1[i]]=lst[lst1[i]]+1

    a=a+1

for i in range(n):
    print(lst[i],end=" ")

print("")