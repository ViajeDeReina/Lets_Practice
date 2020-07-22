# Ch07 > p.221 - Example 02
# SORTING DATA (Harder) : Converting Tuple into Dictionary, and sort the data by the key.

import operator as op # this is essential when it's needed to be sorted by the dictionary key.

trainTupleList = [("Thomas", 5), ("Henry", 8), ("Edward", 9), ("Emily", 5),\
                  ("Thomas", 4), ("Henry", 7), ("Thomas", 3), ("Emily", 8),\
                  ("Percy", 5), ("Gorden", 13)]
trainDic, trainList = {}, []
tmpTup = None
totalRank, currentRank = 1,1

if __name__ == "__main__":
    for tmpTup in trainTupleList:
        tName = tmpTup[0] # get the Name data from [0]th items of trainTupleList
        tWeight = tmpTup[1] # get the Weight data from [1]st items of trainTupleList
        if tName in trainDic:
            trainDic[tName] += tWeight
        else:
            trainDic[tName] = tWeight
    print("기차 수송량 목록 ==> ", trainTupleList)
    print("-----------------------------------")
    trainList = sorted(trainDic.items(), key = op.itemgetter(1), reverse = True)

    print("기차\t총 수송량\t순위")
    print("%10s%10d%10d"%(trainList[0][0], trainList[0][1], currentRank)) #the 1st train
    for i in range(1, len(trainList)): # follwing trains : if having same weight, just pass.
        totalRank +=1
        # totalRank starts from 1 (this is for 1st place), and this for loop starts from 2nd place.
        # need to add 1 when this loop starts to make current Rank.
        if trainList[i][1] == trainList[i-1][1]:
            pass
        # when the weight is same as previous member, we don't need to increase 1 (same current rank)
        else:
            currentRank = totalRank
        # if not same, the Rank should be different, and the increased totalRank will be currentRank.
        print("%10s%10d%10d"%(trainList[i][0], trainList[i][1], currentRank))

