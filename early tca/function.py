
United = False
def is_league_united (hero1,hero2):
    if hero1 == "Superman" and hero2 == "Wonder Woman" or hero1 == "Wonder Woman " and hero2 == "Superman":
        return True
    else :
        return False 





def  decide_plan (hero1,hero2):
    United = is_league_united (hero1,hero2)
    if United == True:
        print("Time to save the world!")
    else:
        print("we must unite the league")    

   
def run ():
    hero1 = str(input("enter the name of the first hero"))
    hero2 = str(input("enter the name of the second hero"))

    print("please enter league or plan")
    Userchoice = str(input())
    if Userchoice == "league":
        United = is_league_united(hero1,hero2)
        print(str(United))
    elif Userchoice == "plan":
        decide_plan (hero1,hero2)
    else :
        print ("Invalid command. Please try again" )


# Run the program
run()
