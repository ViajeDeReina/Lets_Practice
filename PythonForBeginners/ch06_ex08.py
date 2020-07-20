# Ch06 > Exercise 08
# This program will print out star marks by the 2 times of the numbers you input.

i, k, starNum = 0, 0, 0
numStr, ch, starStr = "", "", ""

if __name__ == "__main__":
    numStr = input("숫자를 여러 개 입력하세요 : ")
    print("")
    starStr += "\u2605"
    for i in range (len(numStr)):
        print(starStr * 2 * int(numStr[i]))