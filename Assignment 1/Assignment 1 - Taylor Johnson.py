#Taylor Johnson
#Assignment 1
#August 22, 2016

#This function takes in two variables and outputs basic python arithmetic examples
def Arithmetics():
    print ("This program illustrates arithmetic operators")
    numberOne, NumberTwo = eval(input("Please enter two numbers separated by a comma: "))
    print ("Results of arithmetic on " + str(numberOne) + " and " + str(NumberTwo) + " are given below")
    print ("Sum (+) " + str(numberOne + NumberTwo))
    print ("Difference (-) " + str(numberOne - NumberTwo))
    print ("Product (*) " + str(numberOne * NumberTwo))
    print ("Integer Division (//) " + str(numberOne // NumberTwo))
    print ("Float Division (/) " + str(numberOne / NumberTwo))
    print ("Modulo (%) " + str(numberOne % NumberTwo))
    #input used to keep console open, if not using the IDLE
    input("Press enter to exit")

Arithmetics()
