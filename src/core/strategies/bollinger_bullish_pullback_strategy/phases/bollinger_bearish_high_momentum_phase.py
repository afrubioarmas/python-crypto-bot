import asyncio

from ta.volatility import BollingerBands

from src.core.binance_helpers.binance_client import BinanceClient
from src.core.interval import Interval
from src.core.phase import Phase
from src.core.symbol_pair import SymbolPair
from src.pandas_helper import pandas_helper


class BollingerBearishHighMomentumPhase(Phase):

    def __init__(self, symbolPair: SymbolPair, interval: Interval, stdDev: int):
        super().__init__(symbolPair, interval)
        self.executedPrice = 0
        self.stdDev = stdDev

    async def validate(self) -> bool:

        while True:
            print(
                "Validating phase 0: BollingerBearishHighMomentumPhase for " + self.symbolPair.toString())

            fetchedData = await BinanceClient.client.get_klines(
                symbol=self.symbolPair.toString(),
                interval=self.interval.abbreviate,
                limit=500)

            data = pandas_helper.binanceListToDataFrame(fetchedData)

            indicator_bb = BollingerBands(close=data["Close"][::-1], window=20, window_dev=self.stdDev)

            data["Lower"] = indicator_bb.bollinger_lband()[::-1]
            data["Upper"] = indicator_bb.bollinger_hband()[::-1]

            close = data["Close"].iloc[0]
            open = data["Open"].iloc[0]
            lower = data["Lower"].iloc[0]
            upper = data["Upper"].iloc[0]

            if (((open >= lower) and (close <= lower)) or ((open <= lower) and (close <= lower)) or (
                    (open <= lower) and (close >= lower))) and (upper - lower) > close * 0.02:
                self.executedPrice = close
                return True
            else:
                await asyncio.sleep(self.interval.time)

    async def execute(self):
        print("Phase 0 BollingerBearishHighMomentumPhase: " + self.symbolPair.toString() + " @ " + str(
            self.executedPrice))
