Health = 100
print("Your health is 100%. Escape is in progress..." )
for count in range (0,5,1):
    print("…Oh dear, who is that?"  )
    Userinput = str(input())
    if Userinput == "Smiler's Bot":
        Health = Health - 20
        print("Time to jam out of here!" )
    elif Userinput == "Hacker":
        Health = Health + 20
        print("Yay! Better follow this one!")
    else:
        print("phew just another emoji")

print("Escaped! Health is" + Health)