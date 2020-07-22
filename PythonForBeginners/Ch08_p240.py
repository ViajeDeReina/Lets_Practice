# Ch08 > p.240 - Example 01
# Converting Capital letter into lower case, and visa versa

inStr = input("문자열을 입력하세요 : ")
count = len(inStr)
outStr = ""

for i in range(count):
    ch = inStr[i]
    if (ord(ch)>=ord("A")) & (ord(ch)<=ord("Z")):
        newCh = ch.lower()
    elif (ord(ch)>=ord("a")) & (ord(ch)<=ord("z")):
        newCh = ch.upper()
    else:
        newCh = ch
    outStr += newCh

print("대소문자 변환 결과 --> %s"%outStr)