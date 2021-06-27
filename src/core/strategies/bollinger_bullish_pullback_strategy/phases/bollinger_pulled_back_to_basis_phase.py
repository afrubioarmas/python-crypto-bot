import asyncio

from ta.volatility import BollingerBands

from src.core.binance_helpers.binance_client import BinanceClient
from src.core.interval import Interval
from src.core.phase import Phase
from src.core.symbol_pair import SymbolPair
from src.pandas_helper import pandas_helper


class BollingerPulledBackToBasisPhase(Phase):

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        super().__init__(symbolPair, interval)
        self.executedPrice = 0

    async def validate(self) -> bool:

        while True:
            print("Validating phase 2: BollingerPulledBackToBasisPhase for " + self.symbolPair.toString())
            fetchedData = await BinanceClient.client.get_klines(
                symbol=self.symbolPair.toString(),
                interval=self.interval.abbreviate,
                limit=500)
            data = pandas_helper.binanceListToDataFrame(fetchedData)

            indicator_bb = BollingerBands(close=data["Close"][::-1], window=20, window_dev=self.stdDev)

            data["Basis"] = indicator_bb.bollinger_mavg()[::-1]

            close = data["Close"].iloc[0]
            basis = data["Basis"].iloc[0]

            if close >= basis:
                self.executedPrice = close
                return True
            else:
                await asyncio.sleep(self.interval.time)

    async def execute(self):
        print.sendMessage(
            "Phase 2 BollingerPulledBackToBasisPhase: " + self.symbolPair.toString() + " @ " + str(self.executedPrice))
