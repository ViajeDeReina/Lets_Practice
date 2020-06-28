import sys

x = []
y = []

for i in range (3):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

if (x[0] != x[1]) & (x[0] != x[2]):
    a = x[0]
elif (x[1] != x[2]) & (x[0] != x[1]):
    a = x[1]
else :
    a = x[2]

if (y[0] != y[1]) & (y[0] != y[2]):
    b = y[0]
elif (y[1] != y[2]) & (y[0] != y[1]):
    b = y[1]
else :
    b = y[2]

print(a, b)