import sys

def comp(n):
    prime = [True]*((2*n)+1)
    cnt = 0
    for i in range(2,int((2*n)**0.5)+1):
        if prime[i] == True:
            for j in range(i+i, 2*n+1, i):
                prime[j] = False
    for i in range(n+1, 2*n+1):
        if i==1:
            pass
        elif prime[i] == True:
            cnt +=1
    print(cnt)

n = int(sys.stdin.readline())

while n!=0:
    comp(n)
    n = int(sys.stdin.readline())