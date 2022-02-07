def jon(x):
    s=''
    return s.join(x)


t=input()
lst=list(t)
lst1=[]
for i in lst:
    if i=='l' or i=='o' or i=='v' or i=='e':
        if i in lst1:
            pass
        else:
            lst1.append(i)

a=jon(lst1)
if(a=="love"):
    print("")
else:
    print("")