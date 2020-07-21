#Ch07 > p.219 - Example 01
# SORTING DATA : 1) make random int - 2) convert to HEX - 3) sort by comparing each item

import random as rd

data = []
i, k = 0,0

if __name__ == "__main__":
    for i in range(10):
        tmp = hex(rd.randrange(0, 100000))
        data.append(tmp)
    print("정렬 전 데이터 : ", end=" ")
    [print(num, end=" ") for num in data]

    for i in range(len(data)-1):
        for k in range (i+1, len(data)):
            if int(data[i], 16) > int(data[k], 16):
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp #swap 2 values to make the correct order
    print("\n정렬 후 데이터 : ", end=" ")
    [print(num, end=" ") for num in data]