import sys

a,b,c = map(int, sys.stdin.readline().split())

if b>=c:
    i = -1
else:
    i = a//(c-b)+1

print(i)