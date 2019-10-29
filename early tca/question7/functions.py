def UnderFunction(UserWord):
    print(str(UserWord))
    print("******")

def OverFunction(UserWord):
    print("******")
    print(str(UserWord))

def Both(Userword) :
    print("******",end = "")
    print(str(Userword),end = "")
    print("******",end = "")

def Grid(Userword,n):
    for count in range(0,n,1):
        print("")
        for count2 in range(0,n,1):
            print("******  ", end = "" )
            
        print("")
        for count3 in range(0,n,1):
            print(" " + str(Userword),end=" |")
    print("done")
          

       
  
