

#testList = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


my_file = open("door3-input.txt", "r")
testList = []
content_list = my_file.readlines()
#print(content_list)
for element in content_list:
    testList.append(element.strip())
#print(testList)



def calculateC02(oxygenList, testList, countZero, countOne, indexVar):
    cacheZero = []
    cacheOne = []
    c02List = []
    #print(testList)

    for i in range(0, len(testList)):
        currentBin = testList[i]
        if int(currentBin[indexVar]) == 0:
            countZero +=1
            cacheZero.append(currentBin)
        elif int(currentBin[indexVar]) == 1:
            countOne +=1
            cacheOne.append(currentBin)

    #print(f"Numbers with 0 {cacheZero}\n numbers with 1 {cacheOne}")
    if countZero > countOne:
        c02List = cacheOne

    elif countOne > countZero:
        c02List = cacheZero

    elif countOne == countZero:
        c02List = cacheZero

    #print(c02List)
    countZero = 0
    countOne = 0
    cacheZero = []
    cacheOne = []
    indexVar += 1


    if len(c02List) == 1:
        indexVar = 12

    if indexVar < 12:
        calculateC02(oxygenList, c02List, countZero, countOne, indexVar)

    if indexVar == 12:
        print(f"The C02 rate is {c02List}")

        oxygenInt = (int(oxygenList[0], 2))
        c02Int = (int(c02List[0], 2))

        lifeSupportRating = oxygenInt * c02Int
        print(f"life support rating is {lifeSupportRating}")




def calculateOxygen(testList, countZero, countOne, indexVar):
    cacheZero = []
    cacheOne = []
    oxygenList = []
    my_file = open("door3-input.txt", "r")
    testList2 = []
    content_list = my_file.readlines()
    #print(content_list)
    for element in content_list:
        testList2.append(element.strip())
    #print(testList)

    for i in range(0, len(testList)):
        currentBin = testList[i]
        if int(currentBin[indexVar]) == 0:
            countZero +=1
            cacheZero.append(currentBin)
        elif int(currentBin[indexVar]) == 1:
            countOne +=1
            cacheOne.append(currentBin)

    #print(f"Numbers with 0 {cacheZero}\n numbers with 1 {cacheOne}")
    if countZero > countOne:
        oxygenList = cacheZero

    elif countOne > countZero:
        oxygenList = cacheOne

    elif countOne == countZero:
        oxygenList = cacheOne

    #print(oxygenList)
    countZero = 0
    countOne = 0
    cacheZero = []
    cacheOne = []
    indexVar += 1

    if len(oxygenList) == 1:
        indexVar = 12

    if indexVar < 12:
        calculateOxygen(oxygenList, countZero, countOne, indexVar)

    if indexVar == 12:
        print(f"The oxygen rate is {oxygenList}")
        calculateC02(oxygenList, testList2, 0, 0, 0)

    
calculateOxygen(testList, 0, 0, 0)