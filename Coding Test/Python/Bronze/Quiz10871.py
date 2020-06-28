n, x = map(int, input().split())
list_a = list(map(int,input().strip().split()))[:n]

for i in range(n):
    if list_a[i] < x:
        print(list_a[i], end = " ")