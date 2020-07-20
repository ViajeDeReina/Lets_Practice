# Ch05 > P.137 - Example 1
# Throwing 6 dices at the same time till all the dices have the same number, and counting how many times to throw.

import random as rd

dice1, dice2, dice3, dice4, dice5, dice6 = [0]*6
throwCount, serialCount = 0, 0

if __name__ == "__main__":
    while True:
        throwCount +=1
        dice1 = rd.randrange(1, 7)
        dice2 = rd.randrange(1, 7)
        dice3 = rd.randrange(1, 7)
        dice4 = rd.randrange(1, 7)
        dice5 = rd.randrange(1, 7)
        dice6 = rd.randrange(1, 7)

        if dice1 == dice2 == dice3 == dice4 == dice5 == dice6:
            print("6개의 주사위가 모두 같은 숫자가 나옴 ---> ", dice1, dice2, dice3, dice4, dice5, dice6)
            break
        elif (dice1==1 | dice2==1 | dice3==1 | dice4==1 | dice5==1 | dice6==1)&\
                (dice1==2 | dice2==2 | dice3==2 | dice4==2 | dice5==2 | dice6==2)&\
                (dice1==3 | dice2==3 | dice3==3 | dice4==3 | dice5==3 | dice6==3)&\
                (dice1==4 | dice2==4 | dice3==4 | dice4==4 | dice5==4 | dice6==4)&\
                (dice1==5 | dice2==5 | dice3==5 | dice4==5 | dice5==5 | dice6==5)&\
                (dice1==6 | dice2==6 | dice3==6 | dice4==6 | dice5==6 | dice6==6):
            serialCount +=1
    print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 --> ", throwCount)
    print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속 번호가 나온 횟수 --> ", serialCount)