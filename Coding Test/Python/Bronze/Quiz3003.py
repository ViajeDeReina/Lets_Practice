import sys

shouldbe = [1, 1, 2, 2, 2, 8]
dh_input = list(map(int, sys.stdin.readline().split()))

for i in range (6):
    print(shouldbe[i]-dh_input[i], end=" ")