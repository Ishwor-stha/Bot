# import pandas as pd
import numpy as np

def moving_average_crossover(df, short_window=10, long_window=50):
    df['short_ma'] = df['close'].rolling(window=short_window).mean()
    df['long_ma'] = df['close'].rolling(window=long_window).mean()
    df['signal'] = 0
    df.loc[short_window:, 'signal'] = np.where(
        df['short_ma'][short_window:] > df['long_ma'][short_window:], 1, -1
    )
    return df
