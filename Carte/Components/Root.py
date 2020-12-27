from Carte.State import State

class Root():
    def __init__(self, children):
        self.state = State()
        self.children = children
    def Build(self, _state=None):
        tmp = ""
        for child in self.children:
            tmp += child.Build(self.state) + "\n\n"

        return tmp        