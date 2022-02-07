n=int(input())
sum=0
a=1
for i in range(1,n):
    sum=sum + i
    if(sum<n):
        sum=sum + 2*i
        if(sum<n):
            pass
        elif(sum>=n):
            print("Motu")
            break
    elif(sum>=n):
        print("Patlu")
        break


