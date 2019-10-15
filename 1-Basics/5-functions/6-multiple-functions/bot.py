

def display_ladder (steps):
 
    for Count in range(0,steps,1):
        print( "| |" )
        print( "***" )






def create_ladder():
    steps = int(input("Number of steps?"))
    display_ladder(steps)

create_ladder()