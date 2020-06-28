a, b = map(list, input().split())

a_rev = int(a[2] + a[1] + a[0])
b_rev = int(b[2] + b[1] + b[0])

if a_rev > b_rev:
    print(a_rev)
else:
    print(b_rev)