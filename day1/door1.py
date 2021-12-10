
def checkMeasurment():

    my_file = open("door1-input.txt", "r")
    measurmentList = []
    content_list = my_file.readlines()
    #print(content_list)
    for element in content_list:
        measurmentList.append(element.strip())
    #print(measurmentList)

    isItTheFirst = True
    countIncrease = 0

    for i in range(0, len(measurmentList)):
        currentMeasurment = measurmentList[i]
        lastMeasurment = measurmentList[i-1]

        if isItTheFirst is True:
            print(str(currentMeasurment) + " (N/A - no previous measurement)")
            isItTheFirst = False

        elif int(currentMeasurment) > int(lastMeasurment):
            print(str(currentMeasurment) + " (increased)")
            countIncrease += 1

        elif int(currentMeasurment) < int(lastMeasurment):
            print(str(currentMeasurment) + " (decreased)")

    print(str(countIncrease) + " measurments were larger than the previous")



checkMeasurment()

