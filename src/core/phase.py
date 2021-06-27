from src.core.interval import Interval
from src.core.symbol_pair import SymbolPair


class Phase:

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        self.symbolPair = symbolPair
        self.interval = interval

    async def validate(self) -> bool:
        pass

    async def execute(self):
        pass
