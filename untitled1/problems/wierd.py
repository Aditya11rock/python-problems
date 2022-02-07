n=int(input())
lst=[int(i) for i in input().split()][:n]

sum=0
for i in lst:
    if i%2==0:
        print(i,end=" ")
        sum=sum + i

print(sum,end=" ")
sum=0
for i in lst:
    if i % 2 != 0:
        print(i, end=" ")
        sum = sum + i

print(sum)