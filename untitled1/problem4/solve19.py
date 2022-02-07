from numpy import *
n,m,inn,f=map(int,input().split())
lst=zeros((m,3),int)
for i in range(m):
    a,b,c=map(int,input().split())
    lst[i][0]=a
    lst[i][1] = b
    lst[i][2] = c

lst2=zeros((n,2),int)
for i in range(n):
    a,b=map(int,input().split())
    lst2[i][0]=a
    lst2[i][1]=b

stamina=0
hour=0
while inn<f:
    r=0

    for i in range(m):
        if((lst[i][0]==inn and lst[i][1]>inn)or(lst[i][0]>inn and lst[i][1]==inn)):
            if(stamina<lst[i][2]):
                r=lst[i][2]
                break

            else:
                if(lst[i][0]<lst[i][1]):
                    inn=lst[i][1]
                    stamina=stamina-lst[i][2]
                    if(inn==f):
                        break
                else:
                    inn=lst[i][0]
                    stamina = stamina - lst[i][2]
                    if (inn == f):
                        break


    for i in range(inn-1,n):
        if(stamina<r):
            stamina=lst2[i][0]
            hour=hour + lst2[i][1]


print(hour)