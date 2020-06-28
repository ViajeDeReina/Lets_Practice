a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)
array = list(mul)
array2 = [0,0,0,0,0,0,0,0,0,0]

for i in range (len(array)):
    for j in range (0,10):
        if int(array[i]) == j:
            array2[j] = array2[j] + 1

for i in range (10):
    print(array2[i])