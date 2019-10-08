userinput = int(input(" How many bars should be charged?"))
NoOfBars = 0

while NoOfBars < userinput:
    print("charging :", end = "")
    for Count in range (0,NoOfBars,1):
        print("# ",end = "")

    print("")

    NoOfBars =  NoOfBars + 1

if NoOfBars == userinput:
    print("the battery is fully charged")

