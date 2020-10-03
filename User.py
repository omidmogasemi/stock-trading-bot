import alpaca_trade_api as tradeapi
from Stock import Stock


class User:
    def __init__(self, api_key, secret_key, base_url, tickers):
        self.api = tradeapi.REST(api_key, secret_key, base_url)
        self.account = self.api.get_account()
        self.portfolio = self.api.list_positions()
        print("Welcome to my stock trading bot. Current Buying Power: " +
              self.account.buying_power)

        self.clock = self.api.get_clock()
        self.tickerList = []
        self.stocks = []

        try:
            for i in range((tickers.rindex(","))):
                self.tickerList.append(tickers[i:tickers.index(",")])
                i = tickers.index(",")
        except ValueError:
            self.tickerList.append(Stock(tickers[i:len(tickers)], self.api))

        for i in self.tickerList:
            self.stocks.append(Stock(self.tickerList[i], self.api)
            # might be invalid syntax below
            if self.current_pos=self.api.get_position(self.stocks[i].get_ticker()) != None:
                self.stocks[i].set_current_pos(self.current_pos)

    # poorly named, this is what is called inside of the loop once a minute.
    # here, the bars are extracted from Alpaca's API and then analysis is ran on them
    # and shares are either bought, sold, held, or ignored for the current minute
    def get_bars(self):
        barset=self.api.get_barset(tickers, "1Min", 5)
        for i in self.tickerList:
            self.current_bars=barset[i]
            self.stocks[i].set_barset(self.current_bars)
            self.status=self.stocks[i].analyze_bars()

    def print_portfolio(self):
        print(portfolio)
