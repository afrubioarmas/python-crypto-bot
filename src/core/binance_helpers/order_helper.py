from src.core.binance_helpers.binance_client import BinanceClient
from src.core.binance_helpers.market_info_helper import MarketInfoHelper
from src.core.symbol_pair import SymbolPair


class OrderHelper:

    @staticmethod
    async def marketSellPercentage(symbolPair: SymbolPair, percentage: float = 1):
        balance = await BinanceClient.client.get_asset_balance(asset=symbolPair.pair1.value)

        response = await BinanceClient.client.order_market_sell(
            symbol=symbolPair.toString(),
            quantity=MarketInfoHelper.round(float(balance['free']) * percentage,
                                            MarketInfoHelper.getStepSize(symbolPair)))
        
        return response

    @staticmethod
    async def marketBuyPercentage(symbolPair: SymbolPair, percentage: float = 1):
        balance = await BinanceClient.client.get_asset_balance(asset=symbolPair.pair2.value)

        response = await BinanceClient.client.order_market_buy(
            symbol=symbolPair.toString(),
            quoteOrderQty=MarketInfoHelper.round(float(balance['free']) * percentage,
                                                 MarketInfoHelper.getTickSize(symbolPair)))

        return response
