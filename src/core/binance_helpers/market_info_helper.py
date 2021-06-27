import math

from src.core.binance_helpers.binance_client import BinanceClient
from src.core.symbol import Symbol
from src.core.symbol_pair import SymbolPair


class MarketInfoHelper:
    marketInfo = {}

    @staticmethod
    async def getMarketInfo():

        for symbol in Symbol:
            if (symbol != Symbol.USDT):
                pair = SymbolPair(symbol, Symbol.USDT)
                MarketInfoHelper.marketInfo[pair.toString()] = await BinanceClient.client.get_symbol_info(
                    pair.toString())

    @staticmethod
    def getTickSize(symbolPair: SymbolPair):
        info = MarketInfoHelper.marketInfo
        for actualFilter in info[symbolPair.toString()]["filters"]:
            if actualFilter["filterType"] == "PRICE_FILTER":
                return float(actualFilter["tickSize"])

    @staticmethod
    def getStepSize(symbolPair: SymbolPair):
        info = MarketInfoHelper.marketInfo
        for actualFilter in info[symbolPair.toString()]["filters"]:
            if actualFilter["filterType"] == "LOT_SIZE":
                return float(actualFilter["stepSize"])

    @staticmethod
    def round(amount, precision):
        decimals: int = int(round(-math.log(precision, 10), 0))
        multiplier = 10 ** decimals
        output = math.floor(amount * multiplier) / multiplier
        return output
