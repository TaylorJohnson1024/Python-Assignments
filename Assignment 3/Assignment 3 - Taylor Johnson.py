#Taylor Johnson
#Assignment 3
#September 12, 2016

#This function outputs an 'E' made up of smaller "E's"
#The function takes two inputes, the "E's" width and height
#The "E" itself is composed of 5 parts
#If the user inputs a height non-divisible by 5 than the remainder is appropriately distributed to specific part(s)
#If the user inputs a width non-divisible by 4 than the width is rounded to its nearest integer
def PrintE():
    EWidth, EHeight = eval(input("Enter the width and height of the letter E: "))

    HeightRemainder = EHeight % 5
    Count = 0
    STRINGE = "E"
    EWidth1 = 0
    EWidth2 = 0
    EWidth3 = 0
    EWidth4 = 0
    EWidth5 = 0
    EHeight1 = 0
    EHeight2 = 0
    EHeight3 = 0
    EHeight4 = 0
    EHeight5 = 0

    #Distribution of remaining height lines
    if (HeightRemainder == 1):
        EHeight3 += 1
    elif (HeightRemainder == 2):
        EHeight2 += 1
        EHeight4 += 1
    elif (HeightRemainder == 3):
        EHeight1 += 1
        EHeight3 += 1
        EHeight5 += 1
    elif (HeightRemainder == 4):
        EHeight1 += 1
        EHeight2 += 1
        EHeight4 += 1
        EHeight5 += 1

    #Setting the character limits for each part's width and height
    EWidth1 += EWidth
    EWidth2 += EWidth // 4
    EWidth3 += EWidth // 2
    EWidth4 += EWidth // 4
    EWidth5 += EWidth
    EHeight1 += EHeight // 5
    EHeight2 += EHeight1 + EHeight // 5
    EHeight3 += EHeight2 + EHeight // 5
    EHeight4 += EHeight3 + EHeight // 5
    EHeight5 += EHeight4 + EHeight // 5

    #Assignment just requires "loops", not specifically "for" loops
    #Loop Part 1
    while (Count < EHeight1):
        print(STRINGE * EWidth1)
        Count += 1
    #Loop Part 2
    while (Count < EHeight2):
        print(STRINGE * EWidth2)
        Count += 1
    #Loop Part 3
    while (Count < EHeight3):
        print(STRINGE * EWidth3)
        Count += 1
    #Loop Part 4
    while (Count < EHeight4):
        print(STRINGE * EWidth4)
        Count += 1
    #Loop Part 5
    while (Count < EHeight5):
        print(STRINGE * EWidth5)
        Count += 1

    input("Press enter to close program.")

PrintE()
