from Algorithms.MomentumAlgorithm import MomentumAlgorithm


class Stock:
    ORDER_QUANTITY = 5

    def __init__(self, ticker, api):
        self.ticker = ticker
        self.api = api
        self.current_pos = None
        self.barset = None
        self.algo = None

    def get_ticker(self):
        return self.ticker

    def set_barset(self, barset):
        self.barset = barset
        self.algo = MomentumAlgorithm(
            self.ticker, self.barset, self.current_pos)

    def set_current_pos(self, pos):
        self.temp_pos_aggregate = self.api.get_position(self.ticker)
        # you can choose to extract any necessary information here and pass it into the
        # current position, and then extract it into local vars in the close analysis
        # to use in your custom analysis

        # i should make an abstract class that each algorithm must extend
        # the necessary functions from
        self.current_pos.append(self.temp_pos_aggregate.avg_entry_price)
        self.current_pos.append(self.temp_pos_aggregate.unrealized_pl)

    def analyze_bars(self):
        result = self.algo.perform_analysis()
        if (result == "buy"):
            self.api.submit_order(
                self.ticker, self.ORDER_QUANTITY, "buy", "market", "gtc")
            self.owned = True
        elif (result == "sell"):
            self.api.submit_order(
                self.ticker, self.ORDER_QUANTITY, "sell", "market", "gtc")
            self.owned = False
