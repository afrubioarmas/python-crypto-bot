import asyncio

from src.calculators.lowest_highest_calculator import LowestHighestCalculator
from src.core.binance_helpers.binance_client import BinanceClient
from src.core.interval import Interval
from src.core.phase import Phase
from src.core.symbol_pair import SymbolPair
from src.pandas_helper import pandas_helper
from src.telegram_bot import telegram_bot_helper


class HighestNExitPhase(Phase):

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        super().__init__(symbolPair, interval)
        self.executedPrice = 0

    async def validate(self) -> bool:

        while True:
            print("Validating phase 2: Highest Exit for " + self.symbolPair.toString())
            fetchedData = await BinanceClient.client.get_klines(
                symbol=self.symbolPair.toString(),
                interval=self.interval.abbreviate,
                limit=500)
            data = pandas_helper.binanceListToDataFrame(fetchedData)

            highest = LowestHighestCalculator.highest(data["Close"], 7)
            close = data["Close"].iloc[0]

            if close > highest:
                self.executedPrice = close
                return True
            else:
                await asyncio.sleep(self.interval.time)

    async def execute(self):
        telegram_bot_helper.sendMessage(
            "Phase 2: " + self.symbolPair.toString() + " @ " + str(self.executedPrice))
