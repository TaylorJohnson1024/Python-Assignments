#Author - Taylor Johnson
#Assignment 9
#November 14, 2016

#This program takes an input: two lists
#This program provides an output: the result of both lists added together by index
def add(list1, list2):
    count = 0
    length1 = len(list1)
    length2 = len(list2)

    #choice dependent upon whether the lists are of equal length and which length is longer
    #templist composed of 0s created in same length to longest list
    #loops over numbers from shorter string to templist
    #sets original list equal to templist
    if (length1 != length2):
        if (length1 > length2):
            templist = [0] * length1
            while (count < length2):
                templist[count] = list2[count]
                count += 1
            list2 = templist
        else:
            templist = [0] * length2
            while (count < length1):
                templist[count] = list1[count]
                count += 1
            list1 = templist

    #rests necessary variables
    count = 0
    length1 = len(list1)

    #itterates through each list and adds numbers to their respective index
    while (count < length1):
        list1[count] = list1[count] + list2[count]
        count += 1

    return list1

def main():
    numbers1 = eval(input("Please enter the first set of values: "))
    numbers2 = eval(input("Please enter the first set of values: "))

    print(add(numbers1, numbers2))

main()
