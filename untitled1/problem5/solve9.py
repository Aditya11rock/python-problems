n,k,l,q=map(int,input().split())
dic={}
for i in range(n):
    ls=input()
    lst=[str(j) for j in ls.split()]
    lst2=[]
    for j in range(1,len(lst)):
        lst2.append(int(lst[j]))

    dic[lst[0]]=lst2



while q>0:
    lst=[int(i) for i in input().split()][:k]

    for j in dic.keys():
        lst2=dic.get(j)
        if lst2==lst:
            print(j)
            break
    else:
        print("You cant fool me :P")


    q=q-1

