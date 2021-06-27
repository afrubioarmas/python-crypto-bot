import mplfinance as fplt
import pandas as pd
from ta.volatility import BollingerBands


def plotCandlesticks(data):
    bands = BollingerBands(close=data["Close"], window=20, window_dev=2)

    h_series = pd.Series(bands.bollinger_hband())
    basis_series = pd.Series(bands.bollinger_mavg())
    l_series = pd.Series(bands.bollinger_lband())

    frame = {'HighBB': h_series, 'Basis': basis_series, 'LowBB': l_series}

    result = pd.DataFrame(frame)

    apdict = [fplt.make_addplot(result['HighBB'], color="grey"), fplt.make_addplot(result['Basis'], color="brown"),
              fplt.make_addplot(result['LowBB'], color="grey")]

    fplt.plot(
        data,
        style='charles',
        type='candle',
        title='BTC USDT',
        ylabel='Price ($)',
        datetime_format='%b %d %I:%M %p',
        addplot=apdict
    )
