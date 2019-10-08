userinput = int(input("How many live cables must I avoid"))

Livecables = 0
while userinput >= Livecables:
    print("avoiding")
    Livecables = Livecables + 1
    print("Done!" + str(Livecables) + "live cable avoided")

print("All live cables have been avoided")    