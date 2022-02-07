n=input()
lst=list(n)
sum=0
for i in range(len(n)):
    a=int(lst[i])
    if(a==1):
        sum=sum +2
    elif(a==2):
        sum=sum +5
    elif (a == 3):
        sum = sum +5
    elif (a == 4):
        sum = sum +4
    elif (a == 5):
        sum = sum +5
    elif (a == 6):
        sum = sum +7
    elif (a == 7):
        sum = sum +4
    elif (a == 8):
        sum = sum +7
    elif (a == 9):
        sum = sum +6
    elif (a == 0):
        sum = sum +6

print(sum)
