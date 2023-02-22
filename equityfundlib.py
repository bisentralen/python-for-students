import random

class Fund:
	""" Class for an equity fund """
	# Public class variable (equal for all objects)
	owner_name = "Broke Brokers Inc."

	# Constructor - initializes object
	def __init__(self, fund_name, start_cash=100000.0):
		self._name = fund_name
		self._filename = f"data_fund_{''.join(c for c in self._name if c.isalnum())}.csv"
		self._cash = start_cash
		self._portfolio = {}	# Dict of PortfolioEntry-objects with ticker as key
	
	# Overriding the built-in string representation of a fund object.
	# E.g. what output print(fund_object) gives.
	def __str__(self):
		cash, assets, total = self.get_value()
		cash = "{:.2f}".format(cash); assets = "{:.2f}".format(assets); total = "{:.2f}".format(total)
		fund_summary = f"Name: {self._name}\nOwner: {Fund.owner_name}\nCash value: {str(cash)}\nAssets value: {str(assets)}\nTotal value: {str(total)}"
		return fund_summary

	def portfolio_as_text(self):
		formatted_header = "{:<7} {:<22} {:<14} {:<12} {:<12}".format("Ticker", "Company Name", "Price Bought", "Price Now", "Volume") + "\n"
		formatted_data = ""
		for key, value in self._portfolio.items():
			ticker, company_name, price_bought, price_now, volume = value.to_list()
			formatted_data += "{:<7} {:<22} {:<14.2f} {:<12.2f} {:<12}".format(ticker, company_name, price_bought, price_now, volume) + "\n"
		formatted_portfolio = formatted_header + formatted_data
		return formatted_portfolio

	def load_fund(self):
		""" Read fund data from file """
		df = pd.read_csv(self._filename)
		print(df)

	def save_fund(self):
		""" Save fund data to file """
		print("code missing")

	def buy_stock(self, stock, volume):
		ticker, c_name, price = stock.to_list()
		if ticker in self._portfolio:
			#print(f"Stock {ticker} exists in portfolio")
			self._portfolio[ticker].volume += volume
		else:
			self._portfolio[ticker] = PortfolioEntry(ticker, c_name, price, price, volume)
		# Update cash holding
		self._cash = self._cash - volume*price

	def sell_stock(self, stock, volume="all"):
		ticker, c_name, price = stock.to_list()
		if volume == "all":
			volume = self._portfolio[ticker].volume
			# Update cash holding
			self._cash = self._cash + volume*price
			# Remove entry from portfolio
			self._portfolio.pop(ticker)
		elif 0 <= volume <= self._portfolio[ticker].volume:
			# Update volume
			self._portfolio[ticker].volume -= volume
			# Update cash holding
			self._cash = self._cash - volume*price
		elif volume > self._portfolio[ticker].volume:
			print("Error: Thou cannot sell more than you have. This is not a hedge fund.")

	def update_price(self, ticker, price_new):
		self._portfolio[ticker].price_now = price_new

	def get_value(self):
		cash_value = self._cash
		assets_value = 0
		for ticker, entry in self._portfolio.items():
			assets_value += entry.price_now*entry.volume
		total_value = cash_value + assets_value
		return [cash_value,assets_value,total_value]

	def get_portfolio(self):
		return self._portfolio




class PortfolioEntry:
	""" Class describing an entry/row in a portfolio """
	def __init__(self, ticker, company_name, price_bought, price_now, volume):
		self.ticker = ticker 
		self.company_name = company_name
		self.price_bought = price_bought
		self.price_now = price_now
		self.volume = volume

	def update_price(self, price_new):
		self.price_now = price_new

	def to_list(self):
		return [self.ticker,self.company_name,self.price_bought,self.price_now,self.volume]





class Stock:
	""" Class describing stocks """
	def __init__(self, ticker, company_name, price):
		self._ticker = ticker
		self._company_name = company_name
		self._price = price

	# Get specific data
	def get(self, what):
		if what=='ticker':
			return self._ticker
		elif what=='company_name':
			return self._company_name
		elif what=='price':
			return self._price
		else:
			return f"ERROR: get() takes argument 'ticker', 'company_name', 'price'.\n {what} given"

	# Get all data as a list
	def to_list(self):
		return [self._ticker, self._company_name, self._price]

	# Create new stockprices randomly
	def update_price(self):
		new_price = self._price*(1+random.uniform(-1,1)*5/100)  # 0-5% change (+/-)
		self._price = new_price




if __name__ == "__main__":
    print("Executed when invoked directly")
