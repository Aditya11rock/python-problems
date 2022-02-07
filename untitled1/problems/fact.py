
def fact(x):
    if x==1 or x==0:
        return 1
    else:
        return x*fact(x-1)

t=int(input())
for i in range(t):
    a=int(input())
    b=fact(a)
    print(b)