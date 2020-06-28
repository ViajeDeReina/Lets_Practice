a = list(input().upper())

short_a = list(dict.fromkeys(a))
a_num = []
count = 0

for i in range(len(short_a)):
    count = 0
    for j in range(len(a)):
        if short_a[i] == a[j]:
            count += 1
    a_num.append(count)

dup = a_num.count(max(a_num))

if dup == 1:
    print(short_a[a_num.index(max(a_num))])
else :
    print("?")