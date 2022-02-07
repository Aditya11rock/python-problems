d=int(input())
while d>0:
    x,y,k=map(int,input().split())
    lst=[]
    a=0
    if(x>=y):
        for i in range(y,0,-1):
            if(x%i==0 and y%i==0):
                lst.append(i)
                a=a+1
                if(a==k):
                    break
    else:
        for i in range(x,0,-1):
            if(x%i==0 and y%i==0):
                lst.append(i)
                a=a+1
                if(a==k):
                    break
    if(len(lst)>=k):
        print(lst[k-1])
    else:
        print("No crymeth today")

    d=d-1