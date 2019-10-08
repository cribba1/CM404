factorial = int(input("enter a number"))
RunningTotal = factorial
finalvalue = 1




count = factorial-1
while count > 0:
    RunningTotal = RunningTotal * count
    count-=1
        

print(RunningTotal)

