from math import *
r,g,b=map(int,input().split())
lst=[]
lst.append(r)
lst.append(g)
lst.append(b)
a=min(lst)
if(r==a):
    chance=a
    t=g-a
    if(t%2==0):
        chance=chance + int(t/2)
    else:
        chance=chance + ceil(t/2)

    p=b-a
    if (p % 2 == 0):
        chance = chance + int(p / 2)
    else:
        chance = chance + ceil(p / 2)
    print(chance)
elif(b==a):
    chance = a
    t = g - a
    if (t % 2 == 0):
        chance = chance + int(t / 2)
    else:
        chance = chance + ceil(t / 2)

    p = r - a
    if (p % 2 == 0):
        chance = chance + int(p / 2)
    else:
        chance = chance + ceil(p / 2)

    print(chance)
else:
    chance = a
    t = r - a
    if (t % 2 == 0):
        chance = chance + int(t / 2)
    else:
        chance = chance + ceil(t / 2)

    p = b - a
    if (p % 2 == 0):
        chance = chance + int(p / 2)
    else:
        chance = chance + ceil(p / 2)
    print(chance)