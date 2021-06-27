# from binance import BinanceSocketManager
#
# from src.core.binance_helpers.binance_client import BinanceClient
# from src.core.binance_helpers.market_info_helper import MarketInfoHelper
# from src.core.interval import Interval
# from src.core.phase import Phase
# from src.core.symbol_pair import SymbolPair
# from src.telegram_bot import telegram_bot_helper
#
#
# class TrailingStopFakeBuyPhase(Phase):
#
#     def __init__(self, symbolPair: SymbolPair, interval: Interval, trailing: float):
#         super().__init__(symbolPair, interval)
#         self.trailing = trailing
#
#     async def validate(self) -> bool:
#         self.firstPrice = 0
#         self.bestPrice = 9999999999999999
#         self.executedPrice = 0
#
#         bm = BinanceSocketManager(BinanceClient.client)
#         socket = bm.symbol_ticker_socket(self.symbolPair.toString())
#
#         async with socket as socket:
#             while True:
#                 res = await socket.recv()
#                 recentClosePrice = float(res['c'])
#
#                 if self.firstPrice == 0:
#                     self.firstPrice = recentClosePrice
#
#                 if recentClosePrice < self.bestPrice:
#                     self.bestPrice = recentClosePrice
#
#                 if recentClosePrice > self.bestPrice * (1 + self.trailing):
#                     self.executedPrice = recentClosePrice
#                     return True
#
#                 print("First = " + str(self.firstPrice) +
#                       " TakeProfit = " + str(self.bestPrice * (1 + self.trailing)) +
#                       " Best = " + str(self.bestPrice) +
#                       " Current = " + str(recentClosePrice))
#
#     async def execute(self):
#         profitPercentage = (self.executedPrice * 100 / self.firstPrice) - 100
#         telegram_bot_helper.sendMessage(
#             "Faking trailing buy: " + self.symbolPair.toString() + " @ " + str(self.executedPrice) + " " +
#             MarketInfoHelper.round(str(profitPercentage), 0.001) + "%")
