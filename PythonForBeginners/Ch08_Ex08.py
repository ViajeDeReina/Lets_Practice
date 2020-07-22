# Ch08 > Exercise 08
# this program classifies each type of characters from the string.

sentence = input("문자열을 입력하세요 : ")
length = len(sentence)
upp, low, num, kor, etc = 0, 0 ,0, 0, 0

for i in range (length):
    if (ord(sentence[i]) >=65) & (ord(sentence[i]) <= 90):
        upp += 1
    elif (ord(sentence[i]) >= 97) & (ord(sentence[i]) <= 122):
        low += 1
    elif (ord(sentence[i]) >=48) & (ord(sentence[i]) <= 57):
        num += 1
    elif (ord(sentence[i]) >= ord("ㄱ")) & (ord(sentence[i]) <= ord("힣")):
        kor += 1
    else:
        etc += 1

print("대문자 : %d\t소문자 : %d\t숫자 : %d\t한글 : %d\t기타 : %d"%(upp, low, num, kor, etc))
