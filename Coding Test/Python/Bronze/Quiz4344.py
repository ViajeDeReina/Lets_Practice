c = int(input())

for i in range (c):
    count = 0
    sum = 0
    a = list(map(int,input().split()))
    n = a[0]
    for j in range(1,n+1):
        sum += a[j]
    avg = sum/n
    for k in range (1,n+1):
        if a[k] > avg:
            count +=1
    percent = count/n *100
    print("%.3f" %percent + "%")
    a.clear()
