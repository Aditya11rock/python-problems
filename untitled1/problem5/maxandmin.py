a,b=map(str,input().split())
lst=list(a)
lst1=list(b)
lst2=[]
s=''
for i in range(len(lst1)):
    if lst1[i]=='a' or lst1[i]=="e" or lst1[i]=="i" or lst1[i]=="o" or lst1[i]=="u":
        s=''
    else:
        s=s+lst1[i]
        lst2.append(s)

s=''
lst3=[]
for i in range(len(lst)):
    if lst[i]=='a' or lst[i]=="e" or lst[i]=="i" or lst[i]=="o" or lst[i]=="u":
        s=''
    else:
        s=s+lst[i]
        lst3.append(s)

max=0
for i in lst2:
    if i in lst3:
        e=len(i)
        if(e>max):
            max=e

print(max)