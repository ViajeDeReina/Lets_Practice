# Ch09> p.265 - Practice 13
# Lottery !

import random as rd

def getNum():
    return rd.randrange(1, 46)

lotto = []
num = 0

print("** 로또 추첨을 시작합니다 **")

while True:
    num = getNum()
    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto) >= 6:
        break

print("추첨된 로또 번호 ==> ", end = "")
lotto.sort()
for i in lotto:
    print(i, end = " ")