#Author - Taylor Johnson
#Assignment 7
#October 24, 2016

#This program takes the name of two files
#The program writes a list composed of alternating content from both files into a new file
#First, the file is checked to make sure it exists, program notifies the user if otherwise
#Then, the file is tokenized and transfered to list1, this method allows for empty files and the program
#stops reading after the first blank line
#The second file goes through the same process
#A while loop sorts the lists' elements into the masterList
#Finally, a write function and while loop sets the outfile

#need to use sys.exit to close application after exception
import sys

#base declarations
list1 = []
list2 = []
masterList = []
count = 0

#first file block
try:
    filename1 = input("Enter name of first file: ")
    infile = open(filename1, "r")

    while True:
        line = (infile.readline())

        if (line == '\n' or len(line) == 0):
            infile.close()
            break
        else:
            list1 += line.split()
except FileNotFoundError:
    print ("File not found")
    input("Press enter to close application.")
    sys.exit(1)

#second file block
try:
    filename2 = input("Enter name of second file: ")
    infile = open(filename2, "r")

    while True:
        line = (infile.readline())

        if (line == '\n' or len(line) == 0):
            infile.close()
            break
        else:
            list2 += line.split()
except FileNotFoundError:
    print ("File not found")
    input("Press enter to close application.")
    sys.exit(1)

#setting length of lists to variables
list1Length = len(list1)
list2Length = len(list2)

#alternation of both lists into masterList
#seperate depending upon which list is longer
#had to use append function as other methods were unsatisfactory
if (list1Length >= list2Length):
    while count < list2Length:
        masterList.append(list1[count])
        masterList.append(list2[count])
        count += 1
    while count < list1Length:
        masterList.append(list1[count])
        count += 1
else:
    while count < list1Length:
        masterList.append(list1[count])
        masterList.append(list2[count])
        count += 1
    while count < list2Length:
        masterList.append(list2[count])
        count += 1

#reset count and set name of outfile
count = 0
outfileName = filename1 + filename2

#write masterFile to outfile
outfile = open(outfileName, "w+")
while (count < list1Length + list2Length):
    outfile.write(masterList[count] + '\n')
    count += 1

outfile.close()

input("Your file has been created. Please press enter to exit.")
