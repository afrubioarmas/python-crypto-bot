# import time
#
# from src.core.binance_helpers.binance_client import BinanceClient
# from src.core.interval import Interval
# from src.core.phase import Phase
# from src.core.symbol_pair import SymbolPair
# from src.pandas_helper import pandas_helper
# from src.telegram_bot import telegram_bot_helper
#
#
# class GreenBarFakeBuyPhase(Phase):
#
#     def __init__(self, symbolPair: SymbolPair, interval: Interval):
#         super().__init__(symbolPair, interval)
#         self.executedPrice = 0
#
#     async def validate(self) -> bool:
#
#         while True:
#             fetchedData = await BinanceClient.client.get_klines(
#                 symbol=self.symbolPair.toString(),
#                 interval=self.interval.abbreviate,
#                 limit=100)
#             data = pandas_helper.binanceListToDataFrame(fetchedData)
#
#             close = data["Close"].iloc[-1]
#             open = data["Open"].iloc[-1]
#             if data["Close"].iloc[-1] > data["Open"].iloc[-1]:
#                 self.executedPrice = data["Close"].iloc[-1]
#                 return True
#             else:
#                 time.sleep(1)
#
#     async def execute(self):
#         telegram_bot_helper.sendMessage(
#             "Faking buy: " + self.symbolPair.toString() + " @ " + str(self.executedPrice))
