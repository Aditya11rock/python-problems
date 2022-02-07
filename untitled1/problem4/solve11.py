n=int(input())
lst1=[int(i) for i in input().split()][:n]
lst2=[int(i) for i in input().split()][:n]
a=abs(lst1[1]-lst1[0])
for i in range(1,n-1):
    b=abs(lst1[i+1]-lst1[i])
    if(b>a):
        a=b

c=abs(lst2[1]-lst2[0])
for i in range(1,n-1):
    b=abs(lst2[i+1]-lst2[i])
    if(b>c):
        c=b

if(a>c):
    print("Dom")
    print(a)
elif(c>a):
    print("Brian")
    print(c)
else:
    print("Tie")
    print(a)
