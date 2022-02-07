
n=int(input())

lst=[int(i) for i in input().split()][:n]

even=0
odd=0
for i in range(n-1):
    for j in range(i+1,n):
        if (lst[i]+lst[j])%2==0:
            even=even + lst[i]+lst[j]



for i in range(n-1):
    for j in range(i+1,n):
        if (lst[i]+lst[j])%2!=0:
            odd=odd + lst[i]+lst[j]

if even>odd:
    print(even - odd)

else:
    print(odd - even)