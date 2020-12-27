class Return():
    def __init__(self, target):
        self.target = target
    
    def Build(self, state):
        return f"{state.GetIndentation()}return {self.target.Access(state)};"