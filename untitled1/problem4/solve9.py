n=int(input())
lst=[int(i) for i in input().split()]
a=0
for i in range(n-1):

    while lst[i]!=0:
        lst[i] -=1
        lst[i+1] -=1
        if(lst[i+1]==0 and lst[i]!=1):

            a +=1
            break
    if(a==1):
        break


su=sum(lst)
if(su==0):
    print("YES")
else:
    print("NO")

