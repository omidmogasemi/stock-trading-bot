# This file is meant to test your connection to Alpaca's API by serving as
# a set of API calls whose output is tested to be correct.
# Many of the API calls here are taken directly from the Alpaca Docs to ensure no
# manual errors, however some unique ones are taken directly from classes in this project.
# This file is not run in the actual program.

import os
import sys
import time
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# initialize minute clock system
seconds_elapsed = time.perf_counter()
goal_time = 0

# load environment variables
load_dotenv()
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

# test initial connection
print("TESTING INITIAL ACCOUNT CONNECTION... ")
try:
    api = tradeapi.REST(api_key, secret_key, base_url)
    account = api.get_account()
    print(account)
except:
    print("API/Account connection not established. Please check your environment variables")
    sys.exit()
print("INITIAL ACCOUNT CONNECTION TEST SUCCESSFULLY PASSED.\n")

# test clock system
print("TESTING CLOCK SYSTEM... ")
try:
    clock = api.get_clock()
    print("The market is {}".format("open" if clock.is_open else "closed."))
except:
    print("Could not access the current market clock.")
    sys.exit()
print("CLOCK SYSTEM TEST SUCCESSFULLY PASSED.\n")

# test asset checker
print("TESTING US EQUITITY ASSET CHECKER... ")
try:
    active_assets = api.list_assets(status="active")
    # Please note that list of active US equitity assets are not printed here
    # as it is an incredibly long list that will just make the test flow unreadable in
    # your terminal.
except:
    print("Assets could not be accessed.")
    sys.exit()
print("US EQUITITY ASSET CHECKER TEST SUCCESSFULLY PASSED.\n")

# test live barsets (bars will all have same value is market is closed)
print("TESTING LIVE BARSET TRACKER.. ")
try:
    barset = api.get_barset("SPY,AAPL,QQQ", "1Min", 1)
    print(barset)
    spy_barset = barset["SPY"]
    qqq_barset = barset["QQQ"]
    print(spy_barset)
    print(qqq_barset)
    print("Spy Bar Close Value = ", end="")
    print(spy_barset[0].c)
except:
    print("Could not acquire current bar data sets on SPY, AAPL, and/or QQQ.")
print("LIVE BARSET TRACKER TEST SUCCESSFULLY PASSED.\n")

# test historical data
print("TESTING HISTORICAL BARSET TRACKER... ")
try:
    barset = api.get_barset("AAPL", "day", limit=5)
    aapl_bars = barset["AAPL"]
    week_open = aapl_bars[0].o
    week_close = aapl_bars[-1].c
    percent_change = (week_close - week_open) / week_open * 100
    print('AAPL moved {}% over the last 5 days'.format(percent_change))
except:
    print("Could not acquire historical data for AAPL")
    sys.exit()
print("HISTORICAL BARSET TRACKER TEST SUCCESSFULLY PASSED.\n")

# test placing, cancelling, and selling an order (if the market is open)
print("TESTING ORDERING SYSTEM... ")
clock = api.get_clock()
if clock.is_open:
    try:
        symbol = 'AAPL'
        symbol_bars = api.get_barset(symbol, 'minute', 1).df.iloc[0]
        symbol_price = symbol_bars[symbol]['close']
        api.submit_order(symbol, 1, "buy", "market", "gtc")
        # now add a stop loss and target price
        api.submit_order(symbol, 1, "buy", "market", "gtc", order_class="oco", stop_loss={
                         "stop_price": symbol_price * 0.95},
                         take_profit={"limit_price": symbol_price * 1.05})
        api.submit_order("AAPL", 1, "sell", "market", "gtc")
    except:
        print("There was an error in the order buy/sell process")
        sys.exit()
    print("ORDERING SYSTEM TEST SUCCESSFULLY PASSED.\n")
else:
    print("THE MARKET IS CURRENTLY NOT OPEN. PLEASE TEST AGAIN LATER.\n")

# test reading user portfolio
print("TESTING USER PORTFOLIO... ")
try:
    portfolio = api.list_positions()
    if (portfolio == None):
        print("Your portfolio is currently empty.")
    else:
        for position in portfolio:
            print("{} shares of {}".format(position.qty, position.symbol))
except:
    print("There was an error fetching your portfolio data.")
    sys.exit()
print("USER PORTFOLIO TEST SUCCESSFULLY PASSED\n")

print("\nCONGRATULATIONS, YOU HAVE OFFICIALLY PASSED ALL TESTS. YOUR ACCOUNT AND THE CURRENT EXISTING ALPACA API CALLS ARE WORKING.\n\n")
