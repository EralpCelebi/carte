from Carte.Components.Parts.Derivatives import Accessable

class Addition(Accessable):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def Build(self, state):
        return f"{self.lhs.Access(state)} + {self.rhs.Access(state)}"
    
class Subtraction(Accessable):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def Build(self, state):
        return f"{self.lhs.Access(state)} - {self.rhs.Access(state)}"

class Multiplication(Accessable):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def Build(self, state):
        return f"{self.lhs.Access(state)} * {self.rhs.Access(state)}"

class Division(Accessable):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def Build(self, state):
        return f"{self.lhs.Access(state)} / {self.rhs.Access(state)}"

class Modulus(Accessable):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def Build(self, state):
        return f"{self.lhs.Access(state)} % {self.rhs.Access(state)}"

class Parentheses(Accessable):
    def __init__(self, source):
        self.source = source

    def Build(self, state):
        return f"({self.source.Access(state)})"