class Main ():

    def __init__ (self,name,age,energy,shieldlevel):
        self.name = name
        self.age = age
        self.energy = energy
        self.ShieldLevel = shieldlevel

    def get_age(self):
        age = bot.age
        return age
    def get_energy(self):
        energy = bot.energy
        return energy
    def get_name(self):
        name = bot.name
        return name
    def get_shield(self):
        shield = bot.ShieldLevel
        return shield
    def decrement_energy(self):
        energy = bot.energy
        energy = energy -1 
        return energy
    def decrement_shield(self):
        shield = bot.ShieldLevel
        shield = shield -1
        return shield
    def increment_age(self):
        age = bot.age
        age = age + 1
        return age
    def increment_energy(self):
        energy = bot.energy
        energy = energy + 1 
        return energy
    def increment_shield(self):
        shield = bot.ShieldLevel
        shield = shield + 1
        return shield
    def set_name(self,name):
        bot.name = name
   

    def display_name(self):
        print("******************************")
        print("****" + str(self.name) + "****")
        print("******************************")

    def display_age(self):
        print(str(self.age))

    def display_energy(self):
        energy = self.energy
        print( "energy:\t" + "♦"*energy)
        
    def display_shield(self):
        ShieldLevel = self.ShieldLevel
        print("Shield Level:\t" + "$"*ShieldLevel)

    def display_summary(self):
        self.display_name()
        self.display_age()
        self.display_energy()
        self.display_shield()
        print("displayed all")

    def __str__(self):
        print("Name:" + str(self.name))
        print("Age:" + str(self.age))
        print("Energy:" + str(self.energy))
        print("Shield Level:" + str(self.ShieldLevel))

    
bot = Main("test",18,12,12)
#bot.display_name()
#bot.display_age()
#bot.display_energy()
#bot.display_shield()
#bot.display_summary()
#bot.__str__()