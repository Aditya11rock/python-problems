#n=input()

#def func(s):
#    str1=""
#    return str1.join(s)

#lst=list(n)
#print(*lst)
#print(func(lst))
#str2=func(lst)
#print(str2)
#converting char list to string
from numpy import *
t=int(input())
while t>0:
    n=int(input())
    lst=[int(i) for i in input().split()][:n]


    besti=0
    worst=0
    for i in range(n):
        lst2=[]
        lst2.append(lst[i])
        for j in range(i-1,-1,-1):
            if(lst[j]>lst[i]):
                lst2.append(lst[j])
        lst3=[]
        for j in range(i+1,n):
            for k in lst2:
                if(lst[j]<k):
                    lst3.append(lst[j])
                    break
        for j in range(i-1,-1,-1):
            for k in lst3:
                if(lst[j]>k):
                    if(lst[j] in lst2):
                        break
                    else:
                        lst2.append(lst[j])
                        break


        count=len(lst2) +len(lst3)


        if(i==0):
            besti=count
            worst=count
        elif(count<besti or count>worst):
            if(count<besti):
                besti=count
            else:
                worst=count



    print(besti,end=" ")
    print(worst)

    t=t-1