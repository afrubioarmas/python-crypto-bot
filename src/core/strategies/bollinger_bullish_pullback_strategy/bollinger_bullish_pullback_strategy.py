from src.core.interval import Interval
from src.core.strategies.bollinger_bullish_pullback_strategy.phases.bollinger_bearish_high_momentum_phase import \
    BollingerBearishHighMomentumPhase
from src.core.strategies.bollinger_bullish_pullback_strategy.phases.bollinger_pulled_back_to_basis_phase import \
    BollingerPulledBackToBasisPhase
from src.core.strategies.common.trailing_stop_market_buy_phase import TrailingStopMarketBuyPhase
from src.core.strategies.common.trailing_stop_market_sell_phase import TrailingStopMarketSellPhase
from src.core.strategies.strategy import Strategy
from src.core.symbol_pair import SymbolPair


class BollingerBullishPullbackStrategy(Strategy):

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        super().__init__(symbolPair, interval)
        self.populatePhases()

    def populatePhases(self):
        self.phases.append(BollingerBearishHighMomentumPhase(self.symbolPair, self.interval, 3))
        self.phases.append(TrailingStopMarketBuyPhase(self.symbolPair, self.interval, 0.002))  # 0.002
        self.phases.append(BollingerPulledBackToBasisPhase(self.symbolPair, self.interval))
        self.phases.append(TrailingStopMarketSellPhase(self.symbolPair, self.interval, 0.003))  # 0.004

    def executeFail(self):
        print("Recovering from failure " + self.symbolPair.toString())
