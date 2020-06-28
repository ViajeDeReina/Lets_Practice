import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

totalsec = a+b+c+d
m = totalsec//60
sec = totalsec%60

print(m)
print(sec)