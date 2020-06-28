a = []

for i in range(10):
    n = int(input())%42
    a.append(n)

a = list(dict.fromkeys(a))
print(len(a))