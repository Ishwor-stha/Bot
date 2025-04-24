import MetaTrader5 as mt5
from logic.getHistorical import getData 

# attempt to establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print(f"Failed to initialize, error code = {mt5.last_error()}")
    mt5.shutdown()
else:
    print("MetaTrader 5 initialized successfully.")
    data=getData()
    print(data)
    # You can add more code here in the future to interact with MT5

    # shut down connection to MetaTrader 5 terminal
    mt5.shutdown()
    print("MetaTrader 5 shutdown successfully.")