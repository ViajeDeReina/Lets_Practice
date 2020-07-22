# Ch08 > Exercise 07
# This program eliminates any numeric digit from the string.

sentence = input("문자열 --> ")
length = len(sentence)

print("숫자 제거 -->", end = "")

for i in range (length):
    if (ord(sentence[i]) >=48) & (ord(sentence[i]) <= 57):
        print("", end="")
    else:
        print(sentence[i], end="")