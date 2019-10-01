Name = (input("please enter your name"))
age = int(input("please enter your age"))
weight = int(input("please enter your weight"))
height = float(input("please enter your height"))

def BMI(weight,height):
    bmi = weight/(height*height)
    return bmi
#will ow call bmi

BMItoPrint = BMI(weight,height)
print(BMItoPrint)