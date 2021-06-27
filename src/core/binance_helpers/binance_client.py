import sys

from binance import AsyncClient


class BinanceClient:
    client = 0

    @staticmethod
    async def instanceClient():
        BinanceClient.client = await AsyncClient.create(
            sys.argv[1],
            sys.argv[2]
        )
