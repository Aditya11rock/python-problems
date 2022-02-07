from numpy import *
n=int(input())
lst=[int(i) for i in input().split()][:n]
lst2=zeros((n,2),int)
s,e=map(int,input().split())
for i in range(n):
    lst2[i][0]=lst[i]

while True:
    if(s!=e):
        if(lst2[s-1][1]==0):
            lst2[s-1][1] +=1
            s=lst2[s-1][0]

        elif(lst2[s-1][1]!=0):
            print("No")
            break
    elif(s==e):
        print("Yes")
        break
