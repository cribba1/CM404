
from functions import UnderFunction, OverFunction,Both,Grid



def run ():
    UserWord = str(input("enter your word"))

    print("choose your option")
    print("1.) Under")
    print("2.) Over")
    print("3.) Both")
    print("4.) Grid")
    UserOption = int(input())

    if UserOption == 1:
        UnderFunction(UserWord)
    elif UserOption == 2:    
        OverFunction(UserWord)
    elif UserOption == 3:
        Both(UserWord)
    elif UserOption == 4:
        NumberGridPrint = int(input("enter the size of grid"))
        Grid(UserWord,NumberGridPrint)
    else :
        print ("please enter a number between 1 and 4")

run()