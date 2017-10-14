#Author - Taylor Johnson
#Assignment 10
#November 14, 2016

#This program takes an input: a list of single digits
#This program provides an output: a list of digits not used in the list provided
def search(list, element):
    count = 0
    lengthList = len(list)

    while (count < lengthList):
        if (list[count] == element):
            return True
            break
        else:
            count += 1

    return False

def findMissing(list):
    missing = []
    count = 0

    #iterates 0 ~ 9 using search function, places count in missing if that number is not present
    while (count < 10):
        if (search(list, count) == False):
            missing += [count]
            count += 1
        else:
            count += 1

    return missing

def main():
    myList = eval(input("Enter any list of 0 or more digits in the form [digit, digit, ...]: "))

    print(findMissing(myList))

main()
