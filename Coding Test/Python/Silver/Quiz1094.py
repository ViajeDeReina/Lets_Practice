stick1 = 64
stick2 = 64
count = 1
x = int(input())

while (x<=0) | (x>64):
    x = int(input())

while stick2 != x :

    if x <= stick2:
        stick1 = stick1/2
        stick2 -= stick1
    else:
        stick1 = stick1/2
        stick2 += stick1
        count += 1

print(str(count))