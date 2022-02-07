from math import *
t=int(input())
while t>0:
    n, m, k = map(int, input().split())
    lst = [int(i) for i in input().split()][:n]

    # for i in range(n):
      #  lst[i] = int(pow(lst[i], k))

    ans=int(lst[0])
    for i in range(1,n):
        ans=int((ans * int(lst[i]))/(gcd(ans,int(lst[i]))))

    ans=pow(ans,k)
    s=int(ans %m)
    print(s)

    t=t-1

