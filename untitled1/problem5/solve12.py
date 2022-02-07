t=int(input())
while t>0:
    n=input()
    lst=list(n)
    count=0
    for i in range(len(lst)):
        if(lst[i]=='B'):
            if(i>=2):
                for j in range(i - 1, i-3, -1):
                    if (lst[j] == 'W'):
                        lst[j] = '0'
                        count = count + 1
            else:
                for j in range(i - 1, -1, -1):
                    if (lst[j] == 'W'):
                        lst[j] = '0'
                        count = count + 1
            if(i<=(len(lst)-3)):
                for j in range(i+1,i+3):
                    if(lst[j]=='W'):
                        lst[j]='0'
                        count=count +1
            else:
                for j in range(i+1,len(lst)):
                    if (lst[j] == 'W'):
                        lst[j] = '0'
                        count = count + 1


    print(count)

    t=t-1