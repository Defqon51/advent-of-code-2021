
def checkMeasurment():

    my_file = open("door1-input.txt", "r")
    measurmentList = []
    content_list = my_file.readlines()
    #print(content_list)
    for element in content_list:
        measurmentList.append(int(element.strip()))
    #print(measurmentList)

    counter = 0
    sumMeasurment = 0
    previousSumMeasurment = 0
    nextSumMeasurment = 0

    for i in range(0, len(measurmentList) -2 ):
        #print(str(measurmentList[i]))
        sumMeasurment = sum(measurmentList[i:i+3])
        #print(str(sumMeasurment))
        nextSumMeasurment = sum(measurmentList[i+1:i+4])
        #print(str(nextSumMeasurment))
        if nextSumMeasurment > sumMeasurment:
            counter += 1
            print("increase")

        # Auch eine Möglichkeit es zu lösen, am Ende muss -1 vom Counter abgezogen werden, da der erste Vergleich mit 0 kein increase ist
        #if sumMeasurment > previousSumMeasurment:
        #    counter += 1
        #    print("increase")
        #previousSumMeasurment = sumMeasurment

        
    print(counter)
    #print(counter - 1)



checkMeasurment()

