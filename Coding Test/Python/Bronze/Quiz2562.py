a = []

for i in range(9):
    a.append(int(input()))

print(max(a))

for i in range(9):
    if a[i] == max(a):
        max_num = i+1

print(max_num)