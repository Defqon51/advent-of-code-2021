

my_file = open("door2-input.txt", "r")
commandList = []
content_list = my_file.readlines()
#print(content_list)
for element in content_list:
    commandList.append(element.strip())
#print(commandList)

horizontalPosition = 0
depth = 0
aim = 0

for i in range(0, len(commandList)):
    currentCommand = str(commandList[i])
    if currentCommand.startswith("forward"):
        horizontalPosition += int(currentCommand[-1])
        depth += int(currentCommand[-1]) * aim
    elif currentCommand.startswith("down"):
        aim += int(currentCommand[-1])
    elif currentCommand.startswith("up"):
        aim -= int(currentCommand[-1])


print("the horizontal Position is " + str(horizontalPosition))
print("the depth is " + str(depth))
print(horizontalPosition*depth)
