
t=int(input())
while t>0:
    n,m=map(int, input().split())
    mod=10**9+7
    print(pow(2,m+n-1,mod)-1)

    t=t-1