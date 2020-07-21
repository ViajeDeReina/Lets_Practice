#Ch08 > p.227 - Practice 2

OutStr = ""
inStr = input("문자열을 입력하세요.")
count = len(inStr)

for i in range(count):
    OutStr += inStr[count-(i+1)] #it will read the String from the backward.

print("내용을 거꾸로 출력 --> %s"%OutStr)