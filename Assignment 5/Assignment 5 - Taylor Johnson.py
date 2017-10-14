#Taylor Johnson
#Assignment 5
#October 3, 2016

#This function takes a name of a file and the amount of copies to be made as input
#The function outputs the file's' copies
def copyFile():
    import shutil

    filename = input("Enter the file name to be copied: ")
    amountCopies = eval(input("How many copies?: "))

    #a bunch of variables and methods for making the copied filename match Microsoft copied file naming conventions
    #appears as "test - Copy (4).txt" as for example with "test.txt" being the original filename
    filenameCopyLabel = " - Copy ("
    filenameSplit = filename.split(".")
    filenameLabel = filenameSplit[0]
    filenameExtension = ")." + filenameSplit[1]

    for i in range(amountCopies):
        filenameCopy = filenameLabel + filenameCopyLabel + str(amountCopies) + filenameExtension
        shutil.copyfile(filename, filenameCopy)
        amountCopies -= 1

copyFile()
