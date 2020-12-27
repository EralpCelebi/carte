from Carte.Components.Body import Body
from Carte.State import State

class Argument():
    def __init__(self, typ, name):
        self.typ = typ
        self.name = name
    
    def GetName(self):
        return self.name
        
    def GetType(self):
        return self.typ
    
    def Access(self, state):
        return f"{self.name}"
    
    def Build(self, _state):
        return f"{self.typ.GetType()} {self.name}"

class Function():
    def __init__(self, returns, name, arguments=[]):
        super().__init__()
        self.returns   = returns
        self.name      = name
        self.arguments = arguments
        self.state     = None
        self.body      = Body()

    def Add(self, *parts):
        for part in parts:
            self.body.Add(part)

    def Build(self, state):
        self.state = state.Clone()
        
        for arg in self.arguments:
            self.state.AddVariable(arg.GetName(), arg)

        argmnts = ""
        for i, argument in enumerate(self.arguments):
            if i != 0:
                argmnts += ", "
            argmnts += argument.Build(state)
        argmnts = f"({argmnts})\n"

        tmp = \
            f"{state.GetIndentation()}{self.returns.GetType()} {self.name} {argmnts}"

        tmp += f"{self.body.Build(state)}"

        return tmp

