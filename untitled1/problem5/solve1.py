t=int(input())
lst=[".,?!1","abc2","def3","ghi4","jkl5","mmno6","pqrs7","tuv8","wxyz9","_0"]
while t>0:
    n=input()
    lst2=list(n)
    count=0
    a=0
    for i in lst2:
        lst3=list(lst[a])
        if i in lst3:
            b=0
            for j in range(len(lst3)):
                if i==lst3[j]:
                    b=b+1
                    break
                else:
                    b=b+1
            count=count + b

        else:
            count=count + 1
            for j in range(len(lst)):
                lst4=list(lst[j])
                if i in lst4:

                    a=j
                    b = 0
                    for j in range(len(lst4)):
                        if i == lst4[j]:
                            b = b + 1

                            break
                        else:
                            b = b + 1
                    count = count + b

                    break

    print(count)

    t=t-1