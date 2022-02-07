t = int(input())
while t > 0:
    n = input()
    lst = set(n)
    if len(lst) >= 3 and len(n) > 4:
        print("YES")
    elif len(lst) >= 2 and len(n) >= 7:
        print("YES")
    else:
        print("NO")

    t = t - 1