import sys

album, avg = map(int, sys.stdin.readline().split())
minnum = album * (avg-1) +1

print(minnum)