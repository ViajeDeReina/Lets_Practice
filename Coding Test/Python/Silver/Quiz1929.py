import sys
a, b = map(int, sys.stdin.readline().split())

def comp(a,b):
    prime = [True]*(b+1)
    for i in range(2,int(b**0.5)+1):
        if prime[i] == True:
            for j in range(i+i, b+1, i):
                prime[j] = False
    for i in range(a, b+1):
        if i==1:
            pass
        elif prime[i] == True:
            print(i)

comp(a,b)