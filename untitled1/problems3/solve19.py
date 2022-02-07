t=int(input())
while t>0:
    n=input()
    lst=list(n)
    lst2=[]
    for i in range(len(lst)):
        if(lst[i]=='X'):
            for j in range(i-1,-1,-1):
                if(lst[j]=='O'):
                    lst2.append(j)
                elif(lst[j]=='*'):
                    break
            for j in range(i + 1, len(lst)):
                if (lst[j] == 'O'):
                    lst2.append(j)
                elif (lst[j] == '*'):
                    break
    for j in lst2:
        lst[j]='A'
    c=lst.count('O')
    print(c)

    t=t-1