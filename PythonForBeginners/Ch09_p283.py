# Ch09 > p.283 - Example 01
# Rearranging the HEX data as form of strings & numerical digits

import random as rd

def getNum(strData):
    numStr = ""
    for ch in strData:
        if ch.isdigit():
            numStr += ch # adding on numStr for only numerical digits. other digits will be ignored.
    return int(numStr)

data = []

if __name__ == "__main__":
    for i in range(10):
        tmp = hex(rd.randrange(100000))
        tmp = tmp[2:]
        data.append(tmp)
    print("정렬 전 데이터 : ", end="")
    [print(num, end=" / ") for num in data]

    for i in range(len(data)-1):
        for k in range(i+1, len(data)):
            if getNum(data[i]) > getNum(data[k]):
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp
    print("\n정렬 후 데이터 : ", end= "")
    [print(num, end=" / ") for num in data]