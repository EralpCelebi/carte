from Carte.Components.Parts.Derivatives import Accessable

class Int(Accessable):
    def __init__(self, value=None, **kwargs):
        self.value = value
    
    def Build(self, state):
        return str(self.value)

    def GetValue(self):
        return self.value

    @staticmethod
    def GetType():
        return "int"