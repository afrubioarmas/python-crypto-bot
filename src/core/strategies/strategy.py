from src.core.interval import Interval
from src.core.phase import Phase
from src.core.symbol_pair import SymbolPair


class Strategy:

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        self.symbolPair = symbolPair
        self.interval = interval
        self.currentPhaseIndex = 0
        self.phases = []

    async def execute(self):

        while True:
            try:
                if await self.getCurrentPhase().validate():
                    await self.getCurrentPhase().execute()
                    self.nextPhase()
            except Exception as e:
                print(e)
                self.executeFail()
                self.currentPhaseIndex = 0

    def getCurrentPhase(self) -> Phase:
        return self.phases[self.currentPhaseIndex]

    def nextPhase(self):
        self.currentPhaseIndex += 1
        if self.currentPhaseIndex == len(self.phases):
            self.currentPhaseIndex = 0

    def executeFail(self):
        pass

    def populatePhases(self):
        pass
