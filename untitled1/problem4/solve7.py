t=int(input())
while t>0:
    a,b,c=map(int,input().split())

    d=b-a
    e=c-b
    if(d>=e):
        print(d-1)
    elif(e>d):
        print(e-1)
    elif(e==0 and d==0):
        print('0')