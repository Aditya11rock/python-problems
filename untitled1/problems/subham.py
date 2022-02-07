n=int(input())
lst=[int(i) for i in input().split()][:n]
a=0
for i in range(n-1):
    for j in range(i+1,n):
        if lst[i]^lst[j]==0:
            a+=1

print(a)
