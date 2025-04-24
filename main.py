import MetaTrader5 as mt5
from logic.getHistorical import getData
from logic.movingAverageCrossover import moving_average_crossover

# attempt to establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print(f"Failed to initialize, error code = {mt5.last_error()}")
    mt5.shutdown()
else:
    print("MetaTrader 5 initialized successfully.")
    df=getData()
    # print(df)
    if df is not None:
        df=moving_average_crossover(df)
        print(df[['time', 'close', 'short_ma', 'long_ma', 'signal']])


    # shut down connection to MetaTrader 5 terminal
    mt5.shutdown()
    print("MetaTrader 5 shutdown successfully.")