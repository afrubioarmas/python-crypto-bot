from src.core.interval import Interval
from src.core.strategies.common.trailing_stop_market_buy_phase import TrailingStopMarketBuyPhase
from src.core.strategies.common.trailing_stop_market_sell_phase import TrailingStopMarketSellPhase
from src.core.strategies.lowest_entry_highest_exit_above_ema_strategy.phases.highest_n_exit_phase import \
    HighestNExitPhase
from src.core.strategies.lowest_entry_highest_exit_above_ema_strategy.phases.lowest_n_entry_above_ema_phase import \
    LowestNEntryAboveEmaPhase
from src.core.strategies.strategy import Strategy
from src.core.symbol_pair import SymbolPair


class LowestEntryHighestExitAboveEmaStrategy(Strategy):

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        super().__init__(symbolPair, interval)
        self.populatePhases()

    def populatePhases(self):
        self.phases.append(LowestNEntryAboveEmaPhase(self.symbolPair, self.interval, 300))
        self.phases.append(TrailingStopMarketBuyPhase(self.symbolPair, self.interval, 0.0001))  # 0.002
        self.phases.append(HighestNExitPhase(self.symbolPair, self.interval))
        self.phases.append(TrailingStopMarketSellPhase(self.symbolPair, self.interval, 0.0001))  # 0.004

    def executeFail(self):
        print("Recovering from failure " + self.symbolPair.toString())
