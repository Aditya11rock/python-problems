lst=list(map(int,input().split()))

lst2=list(map(int,input().split()))
coins=int(input())
c=min(lst)

spe=0
ind=lst.index(c)
lst.pop(ind)
co=0
while(lst2[ind]!=0):
    spe=spe + c
    if(spe<=coins):
        co +=1

        lst2[ind] -=1
    else:

        break
lst2.pop(ind)
c=min(lst)
ind=lst.index(c)
lst.pop(ind)

while(lst2[ind]!=0):
    spe=spe + c
    if(spe<=coins):
        co +=1

        lst2[ind] -=1
    else:
        break
lst2.pop(ind)
c=lst[0]
ind=0
lst.pop()

while(lst2[ind]!=0):
    spe=spe + c
    if(spe<=coins):
        co +=1
        lst2[ind] -=1
    else:
        break

print(co)

