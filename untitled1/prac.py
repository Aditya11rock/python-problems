t=int(input())
for i in range(t):
    x,l,n=map(int,input().split())
    p=0
    if n>0:
        while p<x:
            a=x-p
            for j in range(n-1):
                a=a*2

            if a<=l:
                print(p)
                break
            else:
                p+=1
    else:
        print("0")