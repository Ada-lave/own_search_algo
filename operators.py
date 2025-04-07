from atoms import Atom

class Operand:
    left = None
    right = None
    def calculate(self) -> bool:
        pass

class And(Operand):
    def __init__(self, left: Operand | Atom, right: Operand | Atom):
        self.left = left
        self.right = right

    def calculate(self) -> bool:
        return self.left.calculate() and self.right.calculate()
    
    def __str__(self):
        return "AND"

class Or(Operand):
    def __init__(self, left: Operand | Atom, right: Operand | Atom):
        self.left = left
        self.right = right

    def calculate(self) -> bool:
        return self.left.calculate() or self.right.calculate()
    
    def __str__(self):
        return "OR"