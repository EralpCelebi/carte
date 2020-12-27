class Body():
    def __init__(self):
        self.parts = []

    def Add(self, part):
        self.parts.append(part)
    
    def Build(self, state):
        tmp = ""

        state.AddIndentation() 
        for part in self.parts:
            tmp += f"{part.Build(state)}\n"
        state.RemoveIndentation()
        
        template = f"{state.GetIndentation()}"
        template += "{\n%s"
        template += f"{state.GetIndentation()}"
        template += "}"

        tmp = template % tmp

        return tmp