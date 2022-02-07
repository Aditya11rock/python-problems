from math import *
key,value=map(int,input().split())
n=int(input())
lst=[int(i) for i in input().split()][:n]
lst.sort()
sum=int(key * lst[n-1])
c=1
for i in range(n-2,-1,-1):
    if(sum< value):
        sum=int(sum * lst[i])
        c +=1
        if(sum>=value):
            print(c)
            break
    elif(sum>=value):
        print(c)
        break

else:
    print("-1")