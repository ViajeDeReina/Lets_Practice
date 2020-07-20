# Ch06 > p.172 - Example 01
# This program will print out heart marks by the numbers you input.

i, k, heartNum = 0, 0, 0
numStr, ch, heartStr = "", "", ""

if __name__ == "__main__":
    numStr = input("숫자를 여러 개 입력하세요 : ")
    print("")
    heartStr += "\u2665"
    for i in range (len(numStr)):
        print(heartStr * int(numStr[i]))

# Below is the answer code in the book, but I think I could make it better :b

#if __name__ == "__main__":
#    numStr = input("숫자를 여러 개 입력하세요 : ")
#    print("")
#    ch = numStr[i]
#    while True:
#         heartNum = int(ch)
#         heartStr = ""
#         for k in range(0, heartNum):
#             heartStr += "\u2665"
#
#         print(heartStr)
#         i += 1
#         if (i> len(numStr)-1):
#             break
#         ch = numStr[i]