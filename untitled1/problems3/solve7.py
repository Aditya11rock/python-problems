

n=int(input())
lst=[int(i) for i in input().split()][:n]
q=int(input())
while q>0:
    a,b,c=map(int, input().split())
    if(a==0):
        lst[b-1]=c
    elif(a==1):
        no=0
        for i in range(b-1,c):
            if(lst[i]%2==0):
                no +=1

        print(no)
    elif (a == 2):
        no = 0
        for i in range(b - 1, c):
            if (lst[i] % 2 != 0):
                no += 1

        print(no)
    q=q-1