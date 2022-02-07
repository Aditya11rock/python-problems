
n=int(input())
while n>0:
    t=input()
    lst=list(t)
    for i in range(int(len(lst)/2)):
        if(lst[i]!=lst[(len(lst))-i-1]):
            a = ord(lst[0]) - 96
            for i in range(1, len(lst)):
                a = a * (ord(lst[i])-96)
            print(a)
            break
    else:
        print("Palindrome")

    n=n-1

