n=int(input())
lst=[]
while n>0:
    p=input()


    q=int(p[0]+p[1])*100+int(p[3]+p[4])

    r=int(p[6]+p[7])*100+int(p[9]+p[10])
    lstq=[q,r]
    lst.append(lstq)

    n=n-1

for i in range(len(lst)):
    lst2=lst[i]
    mat=True
    for j in range(i+1,len(lst)):
        lst3=lst[j]
        if(lst2[0]<lst3[0]):
            if(lst2[1]>lst3[0]):
                mat=False
                break
        elif(lst2[0]>lst3[0]):
            if(lst2[0]<lst3[1]):
                mat = False
                break

    if mat :
        pass
    else:
        print("Will need a moderator!")
        break
else:
    print("Who needs a moderator?")

