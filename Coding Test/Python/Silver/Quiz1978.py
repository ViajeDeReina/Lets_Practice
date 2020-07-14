import sys
n = int(sys.stdin.readline())
ttl = n
lista = list(map(int, sys.stdin.readline().split()))

for i in lista:
    j = 2
    if i == 1:
        ttl -=1
    while j<i:
        if i ==2:
            break
        elif i%j ==0:
            ttl -=1
            break
        j +=1

print(ttl)