NoToAdd = int(input("how many numbers should i sum up?"))
NumberLookingat = 0
Sum = 0
numberTemp = 0
while NumberLookingat < NoToAdd:
    for count in range(1,NoToAdd + 1,1):
        print("please enter number " + str(count) + "of " + str(NoToAdd) )
        numberTemp = int(input())
        Sum = Sum + numberTemp
    print("the answer is:" + str(Sum))
print("the answer is:" + str(Sum))