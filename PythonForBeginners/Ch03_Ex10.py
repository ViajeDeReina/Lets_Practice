# Ch03 > Exercise 10
# This program will distinguish if the input digit is HEX or not,
# #if it is, it will convert to decimal digit.

a = input("16진수 한글자 입력 : ")
a1 =ord(a)
if (a1 >= 48) & (a1 <= 57):
    print("10진수 ==> %d" % int(a))
elif (a1 >= 65) & (a1 <= 70):
    print("10진수 ==> %d" % int(a,16))
elif (a1 >= 97) & (a1 <= 102):
    print("10진수 ==> %d" % int(a,16))
else:
    print("16진수가 아닙니다.")