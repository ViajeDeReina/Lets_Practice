h,m = map(int, input().split())

if m>=45:
    m = m-45
elif m<45:
    if h == 0:
        h = 23
        m = 15+m
    else:
        h = h-1
        m = 15+m

print(h, m)