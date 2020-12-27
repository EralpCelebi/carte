class Variable():
    def __init__(self, typ, name, value):
        self.typ  = typ
        self.name = name
        self.value= value

    def Access(self, state):
        return f"{self.name}"
    
    def Build(self, state):
        tmp = ""

        state.AddVariable(self.name, self)

        if self.value is not None:
            tmp += f"{state.GetIndentation()}{self.typ.GetType()} {self.name} = {self.value.Access(state)};"
        else:
            tmp += f"{state.GetIndentation()}{self.typ.GetType()} {self.name};"
        
        return tmp

class Get():
    def __init__(self, name):
        self.name = name

    def Access(self, state):
        return state.GetVariable(self.name).Access(state)