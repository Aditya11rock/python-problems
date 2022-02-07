t=input()
sum=0
for i in range(len(t)):
    a=t[i]
    if(a=='0'):
        sum=sum + 6

    elif(a == '1'):
        sum = sum + 2

    elif(a=="2"):
        sum=sum + 5
    elif(a=="3"):
        sum=sum + 5
    elif(a=="4"):
        sum=sum + 4
    elif(a=="5"):
        sum=sum + 5
    elif(a=="6"):
        sum=sum +6
    elif(a=="7"):
        sum=sum + 3
    elif (a=="8"):
        sum=sum + 7
    elif(sum=="9"):
        sum= sum +6

print(sum)