from src.core.interval import Interval
from src.core.strategies.lower_avg_price_strategy.phases.lower_avg_price_phase import LowerAvgPricePhase
from src.core.strategies.strategy import Strategy
from src.core.symbol_pair import SymbolPair


class LowerAvgPriceStrategy(Strategy):

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        super().__init__(symbolPair, interval)
        self.populatePhases()

    def populatePhases(self):
        self.phases.append(LowerAvgPricePhase(self.symbolPair, self.interval))

    def executeFail(self):
        print("Recovering from failure " + self.symbolPair.toString())
