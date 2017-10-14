#Taylor Johnson
#Assignment 6
#October 10, 2016

#This function takes a name of a file to be read
#The function outputs the ending coordinates of the robot, movements provided by file
def robotMovement():
    origin = [0, 0]
    position = origin
    moveList = []

    filename = input("Enter the file name to be copied: ")
    infile = open(filename, "r")

    #turns all lines into a list
    test = (infile.readlines())

    #splits the directions and distance, and gets rid of the \n
    for line in test:
        line.replace("\n", "")
        moveList += line.split()

    #pairs two elements within list
    moveList = list(zip(*[iter(moveList)] * 2))
    #used for testing purposes
    #print (moveList)

    #itterates through directions and modifies the position
    for element in moveList:
        direction = element[0]
        distance = int(element[1])
        if (direction == "N"):
            position[1] += distance
        elif (direction == "NE"):
            position[1] += distance
            position[0] += distance
        elif (direction == "E"):
            position[0] += distance
        elif (direction == "SE"):
            position[1] -= distance
            position[0] += distance
        elif (direction == "S"):
            position[1] -= distance
        elif (direction == "SW"):
            position[1] -= distance
            position[0] -= distance
        elif (direction == "W"):
            position[0] -= distance
        elif (direction == "NW"):
            position[1] += distance
            position[0] -= distance

    #final output
    print ("Final position (" + str(position[0]) + ", " + str(position[1]) + ")")

    input("Please press enter to exit.")
robotMovement()
