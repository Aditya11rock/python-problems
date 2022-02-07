import numpy as np
n=int(input())
while n>0:
    t=int(input())
    b=list(bin(t))

    lst1=np.ones((len(b)-2,1),int)
    lst1[0][0]=0
    lst2=np.zeros((len(b)-2,1),int)
    lst2[0][0]=1
    s=""
    p=""
    for i in range(2,len(b)):
        if b[i]=="0":
            p=p+"1"
            s=s+str(lst1[i-2][0])
        else:
            p=p+str(lst2[i-2][0])
            s = s + str(lst1[i-2][0])


    print(int(s,2)*int(p,2))


    n=n-1