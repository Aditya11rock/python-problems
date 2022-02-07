q=int(input())
while q>0:
    l,r=map(int,input().split())
    count=0
    if(l==1 ):
        for i in range(l+1,r+1):
            lt=str(i)
            lst=list(lt)

            s=''
            for j in range(len(lst)-1,-1,-1):
                w=False
                s=lst[i] +s
                sum=int(s)
                for k in range(2,int(sum/2)+1):
                    if(sum/k==0):
                        break
                else:
                    count +=1
                    w=True
                if w:
                    break
    else:
        s=""
        for i in range(l, r + 1):
            lt = str(i)
            lst = list(lt)

            s=''
            for j in range(len(lst)-1,-1,-1):
                w = False
                s=lst[j] +s
                sum = int(s)
                if(sum==0 or sum==1):
                    pass
                else:
                    for k in range(2, int(sum / 2) + 1):
                        if (sum %k == 0):
                            break
                    else:
                        count += 1

                        w = True
                if w:
                    break
    print(count)

    q=q-1
