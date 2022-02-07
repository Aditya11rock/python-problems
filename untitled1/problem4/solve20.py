from numpy import *
t=int(input())
def jon(x):
    s=''
    for i in range(len(x)):
        s=s+str(x[i][0])
    return s

while t>0:
    n,m=map(int,input().split())
    lsts=[]
    lst=zeros((n+1,1),int)
    z=jon(lst)
    lsts.append(z)

    while m>0:
        q=input()
        lst2=[int(i) for i in q.split()]
        if(lst2[0]==1):
            for i in range(lst2[1],lst2[2]+1):
                if(lst[i][0]==1):
                    lst[i][0]=0
                else:
                    lst[i][0]=1
            z=jon(lst)
            lsts.append(z)
        elif(lst2[0]==2):
            z = jon(lst)
            lsts.append(z)
            lst3 = zeros((n + 1, 1), int)
            for i in range(lst2[1],lst2[2]+1):
                p=lsts[i]
                for j in range(lst2[3],lst2[4]+1):
                    if(p[j]=='1'):
                        lst3[j][0] +=1
            w=0
            sum=0
            for i in range(1,n+1):
                if(lst3[i][0]%2==1):
                    sum +=1
                    if(w==0):
                        w=i
            print(sum,w)
        else:
            z=jon(lst)
            lsts.append(z)
            if (len(lsts) > 1):
                w = lsts[1]
                r = 1
                for i in range(1, len(lsts)):
                    if (lsts[i] > w):
                        w = lsts[i]
                        r = i
                if(w.count('1')>0):
                    print(r)
                else:
                    print('0')

            else:
                print("0")

        m=m-1


    t=t-1