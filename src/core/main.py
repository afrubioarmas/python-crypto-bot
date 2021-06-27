#!/usr/bin/env python3

import asyncio

from src.core.binance_helpers.binance_client import BinanceClient
from src.core.binance_helpers.market_info_helper import MarketInfoHelper
from src.core.interval import Interval
from src.core.orquestrator import Orquestrator
from src.core.strategies.lowest_entry_highest_exit_above_ema_strategy.lowest_entry_highest_exit_above_ema_strategy import \
    LowestEntryHighestExitAboveEmaStrategy
from src.core.symbol import Symbol
from src.core.symbol_pair import SymbolPair


async def main():
    await BinanceClient.instanceClient()
    await MarketInfoHelper.getMarketInfo()
    strategies = []
    for actual in Symbol:
        if (actual != Symbol.USDT):
            strategies.append(
                LowestEntryHighestExitAboveEmaStrategy(SymbolPair(actual, Symbol.USDT), Interval.MINUTE1))
    # strategies.append(LowestEntryHighestExitAboveEmaStrategy(SymbolPair(Symbol.STRAX, Symbol.USDT), Interval.MINUTE30))
    # strategies.append(LowestEntryHighestExitAboveEmaStrategy(SymbolPair(Symbol.ETH, Symbol.USDT), Interval.MINUTE1))

    orq = Orquestrator(strategies)
    # threading.Thread(target=orq.runAll).start()
    await orq.runAll()
    print("bye")


if __name__ == "__main__":
    asyncio.run(main())
