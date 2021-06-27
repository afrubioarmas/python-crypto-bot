import asyncio


class Orquestrator:

    def __init__(self, strategies):
        self.strategies = strategies

    async def runAll(self):
        tasks = []
        for actualStrat in self.strategies:
            t = asyncio.get_event_loop().create_task(actualStrat.execute())
            tasks.append(t)
        await asyncio.gather(*tasks)
