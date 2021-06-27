from backtesting import Strategy
from ta.volatility import BollingerBands

from src.calculators.cross_helper import crossover


class BollingerDowntrendPullbackWithVolatility(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    basisLength = 50

    def init(self):
        # Precompute the two moving averages
        indicator_bb = BollingerBands(close=self.data.df["Close"], window=20, window_dev=2)

        self.upper = indicator_bb.bollinger_hband().to_numpy()
        self.basis = indicator_bb.bollinger_mavg().to_numpy()
        self.lower = indicator_bb.bollinger_lband().to_numpy()

    def next(self):
        index = self.data.index.size

        volatility = (self.upper[index] - self.lower[index]) > (self.data.Close * 0.002)
        isDowntrend = (
                ((self.data.Open >= self.lower[index]) and (self.data.Close <= self.lower[index])) or
                ((self.data.Open <= self.lower[index]) and (self.data.Close <= self.lower[index])) or
                ((self.data.Open >= self.lower[index]) and (self.data.Close >= self.lower[index])))
        if (volatility and isDowntrend):
            self.buy()

        elif crossover(self.data.Close, self.basis[index]):
            self.position.close()
