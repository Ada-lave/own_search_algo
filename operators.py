from atoms import Atom

class Operand:
    def calculate(self) -> bool:
        pass

class And(Operand):
    def __init__(self, left: Operand | Atom, right: Operand | Atom):
        self.left = left
        self.right = right

    def calculate(self) -> bool:
        return self.left.calculate() and self.right.calculate()

class And(Operand):
    def __init__(self, left: Operand | Atom, right: Operand | Atom):
        self.left = left
        self.right = right

    def calculate(self) -> bool:
        return self.left.calculate() or self.right.calculate()