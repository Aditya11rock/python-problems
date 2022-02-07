
n,k,m=map(int,input().split())
lst=[int(i) for i in input().split()][:n]
lst1=[]
for i in range(n):
    lst1.append(0)

lst2=lst
lst2.sort()
a=n-1
print(lst)
while k>0:
    c=0
    for i in range(n):
        if(lst[i]==lst2[a]):
            c=i

            print(lst2[a])
            break

    lst1[c]=lst[c]
    lst[c]=0
    k=k-1
    a=a-1
    


sum=0
b=1

for i in range(n):
    if lst1[i]!=0:
        sum=sum + (lst1[i]*(b%m))
        b=b+1



print(sum)
