import asyncio

from src.core.binance_helpers.binance_client import BinanceClient
from src.core.binance_helpers.order_helper import OrderHelper
from src.core.interval import Interval
from src.core.phase import Phase
from src.core.symbol_pair import SymbolPair
from src.pandas_helper import pandas_helper
from src.telegram_bot import telegram_bot_helper


class LowerAvgPricePhase(Phase):

    def __init__(self, symbolPair: SymbolPair, interval: Interval):
        super().__init__(symbolPair, interval)
        self.isBuy = True
        self.lastPrice = 999999999999999
        self.avgPrice = 0

    async def validate(self) -> bool:

        while True:
            # print("Validating only phase: Improve Avg Price for " + self.symbolPair.toString())
            fetchedData = await BinanceClient.client.get_klines(
                symbol=self.symbolPair.toString(),
                interval=self.interval.abbreviate,
                limit=500)
            data = pandas_helper.binanceListToDataFrame(fetchedData)

            close = data["Close"].iloc[0]

            print(
                "LastPrice: " + str(self.lastPrice) + " BuyLimit: " + str(self.lastPrice * 0.995) + " Sell: " + str(
                    self.lastPrice * 1.001) + " Close: " + str(close))

            if close < self.lastPrice * 0.995:
                self.lastPrice = close
                self.isBuy = True
                return True
            elif close > self.lastPrice * 1.001:
                self.lastPrice = close
                self.isBuy = False
                return True
            else:
                await asyncio.sleep(self.interval.time)

    async def execute(self):
        if self.isBuy:
            response = await OrderHelper.marketBuyPercentage(self.symbolPair, 0.5)
            telegram_bot_helper.sendMessage(
                "Buying Market: " + self.symbolPair.toString() + " @ " +
                str(self.lastPrice))
            await asyncio.sleep(self.interval.time)
        else:
            response = await OrderHelper.marketSellPercentage(self.symbolPair, 0.5)
            telegram_bot_helper.sendMessage(
                "Selling Market: " + self.symbolPair.toString() + " @ " +
                str(self.lastPrice))
            await asyncio.sleep(self.interval.time)
