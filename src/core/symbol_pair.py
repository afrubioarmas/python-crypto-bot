from src.core.symbol import Symbol


class SymbolPair:

    def __init__(self, pair1: Symbol, pair2: Symbol):
        self.pair1 = pair1
        self.pair2 = pair2

    def toString(self):
        return self.pair1.value + self.pair2.value
