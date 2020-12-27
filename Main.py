from Carte.Components.Function import *
from Carte.Components.Parts.Operators import *
from Carte.Components.Parts.Keywords import *
from Carte.Components.Root import *
from Carte.State import State
from Carte.Types import Int
from Carte.Components.Parts.Variable import Get, Variable

main = Function(Int, "main", [Argument(Int,"sup"), Argument(Int,"shit")])
main.Add(
    Variable(Int, "ret", 
        Addition(
            Parentheses(
                Multiplication(
                    Get("sup"),
                    Int(10)
                )
            ),
            Get("shit")
        )
    ),
    Return(Get("ret"))
)
root = Root([main])
print(root.Build())