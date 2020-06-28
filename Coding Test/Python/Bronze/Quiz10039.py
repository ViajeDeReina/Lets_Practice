a = list(map(int, input().split()))
sum = 0

for i in range(5):
    if a[i] <40:
        a[i] = 40
        sum += a[i]
    elif a[i] >= 40:
        sum += a[i]

print(int(sum/5))