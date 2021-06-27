from src.core.interval import Interval
from src.core.strategies.strategy import Strategy
from src.core.strategies.test_strategy.phases.green_bar_fake_buy_phase import GreenBarFakeBuyPhase
from src.core.strategies.test_strategy.phases.red_bar_fake_sell_phase import RedBarFakeSellPhase
from src.core.strategies.test_strategy.phases.trailing_stop_fake_buy_phase import TrailingStopFakeBuyPhase
from src.core.strategies.test_strategy.phases.trailing_stop_fake_sell_phase import TrailingStopFakeSellPhase
from src.core.symbol_pair import SymbolPair


class TestStrategy(Strategy):

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        super().__init__(symbolPair, interval)
        self.populatePhases()

    def populatePhases(self):
        self.phases.append(GreenBarFakeBuyPhase(self.symbolPair, self.interval))
        self.phases.append(TrailingStopFakeBuyPhase(self.symbolPair, self.interval, .0005))
        self.phases.append(RedBarFakeSellPhase(self.symbolPair, self.interval))
        self.phases.append(TrailingStopFakeSellPhase(self.symbolPair, self.interval, .0005))
