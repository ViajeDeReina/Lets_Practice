n = int(input())
correct = []
c = 0
sum = 0

for i in range(n):
    a = list(input().upper())
    for j in range (len(a)):
        if a[j] != "O":
            correct.append(c)
            c = 0
        elif j == len(a)-1:
            c += 1
            correct.append(c)
        elif a[j] == "O":
            c += 1
    for k in range (len(correct)):
        for l in range(1, correct[k]+1):
            sum += l
    print(sum)
    sum = 0
    c = 0
    a.clear()
    correct.clear()