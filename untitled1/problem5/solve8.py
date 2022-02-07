t=int(input())

while t>0:
    m,n=map(int,input().split())
    lst = [1, 1]
    if(n>=m):
        for i in range(2,n):
            lst.append(lst[i-1]+lst[i-2])

        a=lst[m-1]
        b=lst[n-1]
        if(a<=b):
            for i in range(a,0,-1):
                if(a%i==0 and b%i==0):
                    print(i)
                    break
        else:
            for i in range(b,0,-1):
                if(a%i==0 and b%i==0):
                    print(i)
                    break
    else:
        for i in range(2, m):
            lst.append(lst[i - 1] + lst[i - 2])

        a = lst[m - 1]
        b = lst[n - 1]
        if (a <= b):
            for i in range(a, 0, -1):
                if (a % i == 0 and b % i == 0):
                    print(i)
                    break
        else:
            for i in range(b, 0, -1):
                if (a % i == 0 and b % i == 0):
                    print(i)
                    break


    t=t-1