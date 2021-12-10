

#testList = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


my_file = open("door3-input.txt", "r")
testList = []
content_list = my_file.readlines()
#print(content_list)
for element in content_list:
    testList.append(element.strip())
#print(testList)


def calculateEpsilon(gammaRate, epsilonRate, countZero, countOne, indexVar):
    for i in range(0, len(testList)):
        currentBin = testList[i]
        if int(currentBin[indexVar]) == 0:
            countZero +=1
        elif int(currentBin[indexVar]) == 1:
            countOne +=1

    if countZero < countOne:
        epsilonRate = epsilonRate + "0"
    elif countOne < countZero:
        epsilonRate = epsilonRate + "1"

    countZero = 0
    countOne = 0
    indexVar += 1

    if indexVar < 12:
        calculateEpsilon(gammaRate, epsilonRate, countZero, countOne, indexVar)
    if indexVar == 12:
        print("epsilon is " + epsilonRate)

        print(int(epsilonRate, 2))
        print(int(gammaRate, 2))

        powerConsumption = int(epsilonRate, 2) * int(gammaRate, 2)
        print(powerConsumption)




def calculateGamma(gammaRate, countZero, countOne, indexVar):
    for i in range(0, len(testList)):
        currentBin = testList[i]
        if int(currentBin[indexVar]) == 0:
            countZero +=1
        elif int(currentBin[indexVar]) == 1:
            countOne +=1

    if countZero > countOne:
        gammaRate = gammaRate + "0"
    elif countOne > countZero:
        gammaRate = gammaRate + "1"

    countZero = 0
    countOne = 0
    indexVar += 1

    if indexVar < 12:
        calculateGamma(gammaRate, countZero, countOne, indexVar)
    if indexVar == 12:
        print("gamma is " + gammaRate)
        calculateEpsilon(gammaRate, "", 0, 0, 0)

    
calculateGamma("", 0, 0, 0)