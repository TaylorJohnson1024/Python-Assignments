#Taylor Johnson
#Assignment 4
#September 19, 2016

#This function takes the number of lines as input, then lines of text as per input
#The function outputs the lines of text the sorted list of all words found within the lines
def sortSlice():
    listSort = []
    numberLines = eval(input("Enter the number of lines in this document: "))

    for i in range(numberLines):
        line = input("Enter next line: ")
        listSort += line.split()

    listSort.sort()
    for i, word in enumerate(listSort, 1):
        print (i, ")", word)

    input("Please press enter to exit.")

sortSlice()
