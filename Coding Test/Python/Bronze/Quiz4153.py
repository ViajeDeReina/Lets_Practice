import sys
triangle = [1,1,1]
a = 1
b = 1
c = 1
while (a!=0) & (b!=0) & (c!=0):
    a,b,c = map(int, sys.stdin.readline().split())
    triangle[0] = a
    triangle[1] = b
    triangle[2] = c
    if (a==0) & (b==0) & (c==0):
        pass
    elif max(triangle) == a:
        if a**2 == b**2 + c**2:
            print("right")
        else:
            print("wrong")
    elif max(triangle) == b:
        if b**2 == a**2 + c**2:
            print("right")
        else:
            print("wrong")
    else:
        if c**2 == a**2 + b**2:
            print("right")
        else:
            print("wrong")