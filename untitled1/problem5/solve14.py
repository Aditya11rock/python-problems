t=int(input())
while t>0:
    n,k=map(int,input().split())
    lst=[int(i) for i in input().split()][:n]

    for i in range(n):
        tan=False
        if(lst[i]%k==0):
            pass
        else:
            man=True
            for j in range(i+1,len(lst)):
                if((lst[i]+lst[j])%k==0):
                    man=False
                    break
            if man:
                for j in range(i-1,-1,-1):
                    if ((lst[i] + lst[j]) % k == 0):

                        break
                else:
                    tan=True

        if tan:
            print("NO")
            break
    else:
        print("YES")



    t=t-1