t=int(input())
while t>0:
    s=input()
    bet=len(s)
    lst=[]
    lst.append(s[0])
    d=0
    for i in range(1,bet):
        if(s[i]==')'):
            if d!=-1:
                a=lst[d]
                if(a=='('):
                    c=lst.pop()
                    d=d-1
                else:
                    lst.append(s[i])
                    d=d+1
            else:
                lst.append(s[i])
                d=d+1
        elif (s[i] == ']'):
            if d!=-1:
                a=lst[d]
                if (a == '['):
                    c = lst.pop()
                    d = d - 1
                else:
                    lst.append(s[i])
                    d = d + 1
            else:
                lst.append(s[i])
                d=d+1
        elif (s[i] == '}'):
            if d!=-1:
                a=lst[d]
                if (a == '{'):
                    c = lst.pop()
                    d = d - 1
                else:
                    lst.append(s[i])
                    d = d + 1
            else:
                lst.append(s[i])
                d=d+1
        else:
            lst.append(s[i])
            d=d+1

    if(d!=-1):
        print("NO")
    else:
        print("YES")

    t=t-1