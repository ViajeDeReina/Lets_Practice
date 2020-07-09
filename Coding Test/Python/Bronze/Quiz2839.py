import sys

n = int(sys.stdin.readline())

ab = []

for i in range (n):
    for j in range (n):
        sum = 5*i + 3*j
        if sum == n:
            ab.append(i+j)

if len(ab) ==0:
    print(-1)
else:
    print(min(ab))