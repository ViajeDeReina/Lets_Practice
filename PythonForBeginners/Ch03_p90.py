# Ch03 > P.99 - Example02
# This program will convert the string into reversed form
# ex > apple --> elppa

inStr = ""

if __name__ == "__main__":
    inStr = input("문자열을 입력 --> ")
    for i in range(len(inStr)-1, -1, -1):
        print(inStr[i], end = "")