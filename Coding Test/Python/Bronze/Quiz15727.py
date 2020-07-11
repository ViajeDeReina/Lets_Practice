import sys
distance = int(sys.stdin.readline())

if distance%5 == 0:
    time = distance//5
else:
    time = distance//5 +1

print(time)