n = int(input())

if n<10:
    a = 0
    b = n
elif n >=10:
    a = int(str(n)[0])
    b = int(str(n)[1])

c = a + b
new_num = int(str(b)[-1] + str(c)[-1])
cnt = 1

while new_num != n:
    if new_num <10:
        a = 0
        b = new_num
    elif new_num >=10:
        a = int(str(new_num)[0])
        b = int(str(new_num)[1])
    c = a + b
    new_num = int(str(b)[-1] + str(c)[-1])
    cnt += 1

print(cnt)