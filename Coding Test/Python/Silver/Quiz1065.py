n = int(input())
ttl = 0
count_num = []

for i in range(1, n+1):
    count = 0
    a = list(str(i))
    for k in range (len(a)):
        count_num.append(-1)
    if len(a) <= 2:
        ttl += 1
    else:
        dif = int(a[1])-int(a[0])
        for j in range(len(a)-1):
            if int(a[j+1])-int(a[j]) == dif:
                count += 1
            count_num[j] = count
        if count_num[j] == len(a)-1:
            ttl += 1

print(ttl)