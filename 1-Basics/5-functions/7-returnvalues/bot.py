

def sum_weights(Weight1, weight2):
    Total = Weight1 + weight2
    return Total


def calc_avg_weight(Weight1, Weight2):
    Total = Weight1 + Weight2
    Average = Total/2
    return Average

def run():

    Userinput = input("enter sum or average")

    if  Userinput == "sum":
        Weight1 = int(input("beep weight"))
        Weight2 = int(input("bop weight"))
        Sum = sum_weights(Weight1,Weight2)
        print(str(Sum)) 
    elif Userinput == "average":
        Weight1 = int(input("beep weight"))
        Weight2 = int(input("bop weight"))
        Average = calc_avg_weight(Weight1, Weight2)
        print(str(Average))
run()