import pandas as pd
from pandas import DataFrame


def binanceListToDataFrame(list):
    output = DataFrame(list,
                       columns=["OpenDate", "Open", "High", "Low", "Close", "Volume", "CloseTime", "QuoteAssetVolume",
                                "NumTrades", "TakerBuyBaseAssetVolume ", "TakerBuyQuoteAssetVolume", "Ignore"])
    output["Close"] = pd.to_numeric(output["Close"])
    output["Open"] = pd.to_numeric(output["Open"])
    output["Low"] = pd.to_numeric(output["Low"])
    output["High"] = pd.to_numeric(output["High"])
    output["Volume"] = pd.to_numeric(output["Volume"])
    output["OpenDate"] = pd.to_datetime(output["OpenDate"], unit='ms')
    output["OpenDate"] = pd.DatetimeIndex(output["OpenDate"]).tz_localize("UTC").tz_convert("America/Caracas")
    output = output.set_index('OpenDate')
    return output[::-1]


def binanceListToDataFrameForBackTest(df):
    output = binanceListToDataFrame(df)[["Close", "Open", "Low", "High", "Volume", "datetime"]]
    output["Close"] = pd.to_numeric(output["Close"])
    output["Open"] = pd.to_numeric(output["Open"])
    output["Low"] = pd.to_numeric(output["Low"])
    output["High"] = pd.to_numeric(output["High"])
    output["Volume"] = pd.to_numeric(output["Volume"])
    output["datetime"] = pd.to_datetime(output["datetime"], unit='ms')
    output["datetime"] = pd.DatetimeIndex(output["datetime"]).tz_localize("UTC").tz_convert("America/Caracas")
    output = output.set_index('datetime')
    return output[::-1]
