t=int(input())
while t>0:
    n,m=map(int , input().split())
    while n>0:
        a=1
        z=100
        e,f,g=map(int,input().split())
        price=z-e
        price=price-((price * f)/100)
        price=price-((price * g)/100)
        k=a
        z=100

        while(a<m):
            a=a+1
            b,c,d=map(int,input().split())
            price2=z-b
            price2=price2-((price2 * c)/100)
            price2=price2-((price2 * d)/100)

            if price2<price:
                price=price2
                k=a
            z=100

        print(k,end=" ")
        n=n-1
    print()
    t=t-1