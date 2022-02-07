from itertools import *


n=int(input())
lst=[int(i) for i in input().split()][:n]
q=int(input())
while q>0:
    p=int(input())
    ans=0
    if(p>0):
        ans=sum(lst)
        for i in range(2,p+1):
            lst2=list(combinations(lst,2))
            for j in range(len(lst2)):
                pt=lst2[j]
                a=pt[0]
                for k in range(1,len(pt)):
                    a=a^pt[k]

                ans=ans+a
        ans=ans%(998244353)
        print(ans)
    q=q-1


