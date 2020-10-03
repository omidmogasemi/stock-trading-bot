class MomentumAlgorithm:

    def __init__(self, ticker, barset, current_pos):
        self.barset = barset
        self.current_pos = current_pos
        self.ticker = ticker

    def perform_analysis(self):
        if self.current_pos == None:
            self.perform_close_analysis()
        else:
            self.perform_open_analysis()

    def perform_open_analysis(self):

        # implement actual algorithm here

        return

    def perform_close_analysis(self):
        self.entry_price = self.current_pos[0]
        self.pl = self.current_pos[0]

        # implement actual algorithm here

        return
