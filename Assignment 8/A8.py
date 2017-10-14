#Author - Taylor Johnson
#Assignment 8
#October 31, 2016

#This program takes an input: name of a file
#This program provides an output: average of temperature(s), from data given, in reverse order

#need to use sys.exit to close application after exception
import sys

#base declarations
listTemperatures = []
listTemporary = []
listAvgTemperatures = []
count = 0
subCount = 0

#catches nonexistent files
try:
    filename1 = input("Enter name of first file: ")
    infile = open(filename1, "r")

    #loops through each line
    while True:
        line = (infile.readline())

        #partitions data before 'NEXT\n' into sublists
        if (line == 'NEXT\n' or line == 'NEXT'):
            #if not empty
            if (listTemporary != []):
                listTemperatures.append(listTemporary)
                listTemporary = []

        #loop stops at blank line
        elif (line == '\n' or len(line) == 0 or line == ""):
            #if not empty
            if (listTemporary != []):
                listTemperatures.append(listTemporary)
                listTemporary = []
            infile.close()
            break

        else:
            listTemporary += line.split()

except FileNotFoundError:
    print ("File " + filename1 + " not found")
    input("Press enter to close application.")
    sys.exit(1)

#loops through years and cleans average variable
while count < len(listTemperatures):
    average = 0

    #loops through data within year
    #sets data to int data type and adds them to average variable
    while subCount < len(listTemperatures[count]):
        average += int(listTemperatures[count][subCount])
        subCount += 1

    #average variable is set as the average of data and appends data to list
    average = average / len(listTemperatures[count])
    listAvgTemperatures.append(average)
    count += 1
    subCount = 0

#count set in preperation for print list in reverse order
count = len(listAvgTemperatures) - 1

while count >= 0:
    print(listAvgTemperatures[count])
    count -= 1
