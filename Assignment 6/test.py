
listSort = []

infile = open("move.txt", "r")

test = (infile.readlines())
print (test)

for line in test:
    line.replace("\n", "")
    listSort += line.split()
    print (line)
print (listSort)

listSort = list(zip(*[iter(listSort)] * 2))
print (listSort)

for element in listSort:
    print (element[0])
    print (element[1])

infile.close()
input("Please press enter to exit.")
