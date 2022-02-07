n=int(input())
lst=[int(i) for i in input().split()][:n]
total=sum(lst)
each=int(total/n)
cost=0

for i in range(n):
    while lst[i]<each:
        if(i==0):
            if(lst[n-1]>each):
                cost=cost + 1
                lst[n-1] +=1
                lst[i] +=1
            else:
                lst[i] +=1
                lst[i+1] -=1
                cost +=1
        else:
            lst[i] +=1
            cost +=1
            lst[i+1] -=1
    while lst[i]>each:
        if(i<n-1):
            lst[i] -=1
            cost +=1
            lst[i+1] +=1
        else:
            lst[i] -=1
            lst[i-1] +=1
            cost +=1



print(cost)
