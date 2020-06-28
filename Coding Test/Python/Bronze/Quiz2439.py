n = int(input())
for i in range(0,n):
    for j in range(1,n+1):
        if (n-j) <= i:
            print("*",end="")
            if j == n:
                print("")
        else:
            print(" ",end="")