
t=int(input())
while t>0:
    x,y,z=map(float,input().split())
    a=float((x-y +z)/2)
    b=float((x+y-z)/2)
    c=float((y+z-x)/2)
    area=float((a*b)+(b*c)+(a*c))
    area=float(area *2)
    area=round(area,4)
    print(area)

    t=t-1