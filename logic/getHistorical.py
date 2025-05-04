# getHistorical.py
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta



def getData():
    # Define the symbol and timeframe
    symbol = "XAUUSD"
    timeframe = mt5.TIMEFRAME_H1
    num_bars = 100

    # Timeframe mapping
    # M1: 1-minute chart (each candlestick represents 1 minute of price data).
    # M5: 5-minute chart.
    # M15: 15-minute chart.
    # M30: 30-minute chart.
    # H1: 1-hour chart.
    # H2: 2-hour chart.
    # H4: 4-hour chart.
    # D1: Daily chart (1 day per candlestick).
    # W1: Weekly chart (1 week per candlestick).
    # MN1: Monthly chart (1 month per candlestick).
    TIMEFRAME_STR = {
        mt5.TIMEFRAME_M1: "M1",
        mt5.TIMEFRAME_M5: "M5",
        mt5.TIMEFRAME_M15: "M15",
        mt5.TIMEFRAME_M30: "M30",
        mt5.TIMEFRAME_H1: "H1",
        mt5.TIMEFRAME_H2: "H2",
        mt5.TIMEFRAME_H4: "H4",
        mt5.TIMEFRAME_D1: "D1",
        mt5.TIMEFRAME_W1: "W1",
        mt5.TIMEFRAME_MN1: "MN1",
    }
    pd.set_option('display.max_rows', None)


    # Request historical data
    # rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
    start = datetime.now() - timedelta(days=365*5)
    rates = mt5.copy_rates_from("XAUUSD", mt5.TIMEFRAME_H4, start, 10000)
    # print(rates)

    # Process the received data
    if rates is not None and len(rates) > 0:
        # Convert the NumPy array to a Pandas DataFrame for easier handling
        df = pd.DataFrame(rates)

        # Convert the 'time' column from seconds since epoch to datetime objects
        df['time'] = pd.to_datetime(df['time'], unit='s')

        # Get the string representation of the timeframe from  mapping
        timeframe_str = TIMEFRAME_STR.get(timeframe, str(timeframe))

        print(f"Retrieved {len(df)} bars of historical data for {symbol} in {timeframe_str} timeframe:")

        return df
    else:
        print(f"Failed to retrieve historical data for {symbol}, error code = {mt5.last_error()}")

