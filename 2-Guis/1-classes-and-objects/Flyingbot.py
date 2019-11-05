from superbot import SuperBot
class FlyingBot(SuperBot):
    def __init__ (self,name,age,energy,shield,Super_Power_Level,hover=1234567890):
        super().__init__(name,age,energy,shield,Super_Power_Level)
        self.hover = hover
    def get_hover_distance(self):
        hover = self.hover
        return hover
    def set_hover_distance(self,hover):
        self.hover = hover
    

Gary = FlyingBot("gary","",420,45324,12222222222)
value = Gary.get_hover_distance()
print(str(value))