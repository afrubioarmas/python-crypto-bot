import asyncio

import ta.trend

from src.calculators.lowest_highest_calculator import LowestHighestCalculator
from src.core.binance_helpers.binance_client import BinanceClient
from src.core.interval import Interval
from src.core.phase import Phase
from src.core.symbol_pair import SymbolPair
from src.pandas_helper import pandas_helper


class LowestNEntryAboveEmaPhase(Phase):

    def __init__(self, symbolPair: SymbolPair, interval: Interval, movingAverageLength: int):
        super().__init__(symbolPair, interval)
        self.executedPrice = 0
        self.movingAverageLength = movingAverageLength

    async def validate(self) -> bool:

        while True:
            print(
                "Validating phase 0: LowestNEntryAboveEma for " + self.symbolPair.toString())

            fetchedData = await BinanceClient.client.get_klines(
                symbol=self.symbolPair.toString(),
                interval=self.interval.abbreviate,
                limit=301)

            data = pandas_helper.binanceListToDataFrame(fetchedData)

            lowest = LowestHighestCalculator.lowest(data["Close"], 7)
            close = data["Close"].iloc[0]

            ema = ta.trend.EMAIndicator(close=data["Close"][::-1], window=self.movingAverageLength)
            data["MovingAverage"] = ema.ema_indicator()[::-1]
            movingAverage = data["MovingAverage"].iloc[0]

            # print(tabulate(data, headers='keys', tablefmt='psql'))

            # if close < lowest and close > movingAverage:
            if True:
                self.executedPrice = close
                return True
            else:
                await asyncio.sleep(self.interval.time)

    async def execute(self):
        print("Phase 0: " + self.symbolPair.toString() + " @ " + str(self.executedPrice))
