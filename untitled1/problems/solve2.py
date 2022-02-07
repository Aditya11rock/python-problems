t=int(input())
while t>0:
    st1=input()
    st2=input()
    c=len(st1)
    d=len(st2)
    for i in range(c):
        e=st1[i]

        for j in range(d):
            if st2[j]<e:
                f=st2[j]
                l=''
                for k in range(c):
                    if k==i:
                        l=l+f
                    else:
                        l=l+st1[k]
                del(st1)
                st1=''
                st1=st1 +l
                z=''
                for m in range(d):
                    if m==j:
                        z=z +'}'
                    else:
                        z=z + st2[m]
                del(st2)
                st2=''
                st2=st2 +z
                break


    print(st1)
    t=t-1
