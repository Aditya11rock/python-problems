n=int(input())
vaccines=[int(i) for i in input().split()][:n]
patient=[int(i) for i in input().split()][:n]
vaccines.sort()
patient.sort()
for i in range(n):
    if patient[i]<vaccines[i]:
        print("No")
        break
else:
    print("Yes")

