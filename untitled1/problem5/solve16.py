t=int(input())
while t>0:
    n=input()
    q=int(input())
    s=""
    lst=list(n)
    val=0
    if((lst[6]+lst[7])=="AM"):
        if(int(lst[0]+lst[1])==12):
            val=int(lst[3]+lst[4])
        else:
            val=int(lst[0]+lst[1])*100+int(lst[3]+lst[4])
    else:
        if(int(lst[0]+lst[1])==12):
            val = int(lst[0] + lst[1]) * 100 + int(lst[3] + lst[4])
        else:
            val = int(lst[0] + lst[1]) * 100 + int(lst[3] + lst[4])+1200
    while q>0:
        p=input()
        lst2=list(p)
        a=0
        b=0
        if((lst2[6]+lst2[7])=="AM"):
            if(int(lst2[0]+lst2[1])==12):
                a=int(lst2[3]+lst2[4])
            else:
                a=int(lst2[0]+lst2[1])*100+int(lst2[3]+lst2[4])
        else:
            if(int(lst2[0]+lst2[1])==12):
                a=int(lst2[0]+lst2[1])*100+int(lst2[3]+lst2[4])
            else:
                a=int(lst2[0]+lst2[1])*100+int(lst2[3]+lst2[4])+1200
        if((lst2[15]+lst2[16])=="AM"):
            if(int(lst2[9]+lst2[10])==12):
                b=int(lst2[12]+lst2[13])
            else:
                b=int(lst2[9]+lst2[10])*100+int(lst2[12]+lst2[13])
        else:
            if (int(lst2[9] + lst2[10]) == 12):
                b = int(lst2[9] + lst2[10]) * 100 + int(lst2[12] + lst2[13])
            else:
                b=int(lst2[9]+lst2[10])*100+int(lst2[12]+lst2[13])+1200

        if a<=val and val<=b:
            s=s+"1"
        else:
            s=s+"0"
        q=q-1

    print(s)

    t=t-1