


Word = str(input("please enter a word"))
print (" please choose one of the following")
print ("1) Display in a Box – display the word in an ascii art box ")
print("2) Display Lower-case – display the word in lower-case e.g. hello ")
print("3) Display Upper-case – display the word in upper-case e.g. HELLO ")
print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH ")
print("5) Repeat the word x times")

def switch_case(ChoiceNo)
    switcher = {
        1:BoxDisplay(Word)
        2:LowerCase(Word)
        3:
        4:
        5:







    }

def BoxDisplay(Word):
    print ("!!!!!!!!!!")
    print ("!"      "!")
    print ("!" +Word + "    !")
    print ("!!!!!!!!!!")

def LowerCase(Word):
    Lower = Word.lower()
    return Lower

def UpperCase(Word):
    Upper = Word.upper()
    return Upper

def Mirrored(Word):
    Split = Word.split(',')
    for count in range(len(Word)-1 , -1, -1):
        print(Word[count],end=)