#!/usr/bin/env python3

import asyncio

from src.core.binance_helpers.binance_client import BinanceClient
from src.core.binance_helpers.market_info_helper import MarketInfoHelper
from src.core.interval import Interval
from src.core.orquestrator import Orquestrator
from src.core.strategies.lower_avg_price_strategy.lower_avg_price_strategy import LowerAvgPriceStrategy
from src.core.symbol import Symbol
from src.core.symbol_pair import SymbolPair


async def main():
    await BinanceClient.instanceClient()
    await MarketInfoHelper.getMarketInfo()
    strategies = []
    # for actual in Symbol:
    #     if (actual != Symbol.USDT):
    #         strategies.append(
    #             LowestEntryHighestExitAboveEmaStrategy(SymbolPair(actual, Symbol.USDT), Interval.MINUTE30))

    strategies.append(LowerAvgPriceStrategy(SymbolPair(Symbol.BTC, Symbol.USDT), Interval.MINUTE1))
    # strategies.append(LowestEntryHighestExitAboveEmaStrategy(SymbolPair(Symbol.ETH, Symbol.USDT), Interval.MINUTE1))

    orq = Orquestrator(strategies)
    # threading.Thread(target=orq.runAll).start()
    await orq.runAll()


if __name__ == "__main__":
    asyncio.run(main())
