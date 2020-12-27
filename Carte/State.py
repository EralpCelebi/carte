class State():
    def __init__(self):
        self.tab = "    "
        self.indent = 0
        
        self.variables = {}
    
    def Clone(self):
        tmp = State()
        tmp.indent = self.indent
        tmp.variables = self.variables

        return tmp

    def AddVariable(self, name, source):
        self.variables[name] = source
    
    def GetVariable(self, name):
        return self.variables[name]

    def AddIndentation(self):
        self.indent += 1

    def RemoveIndentation(self):
        if(self.indent > 0):
            self.indent -= 1
    
    def GetIndentation(self):
        return self.tab * self.indent

