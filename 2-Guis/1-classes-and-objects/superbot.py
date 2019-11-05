
from bot import Main
class SuperBot(Main):
    def __init__ (self,name,age,energy=69,shield=69,Super_Power_Level=69):
        super().__init__(name,age,energy,shield)
        self._Super_Power_Level = Super_Power_Level
        

    def get_super_power_level(self):
        Super_Power_Level = self.Super_Power_Level

        return Super_Power_Level
    def set_super_power_level(self,Super_Power_Level):
        self.Super_Power_Level = Super_Power_Level 

Gary = SuperBot("gary","",420,45324,12222222222)
value = Gary.get_super_power_level()
print(str(value))
