"""
	Author: Luis_C-137
	This API comunicates with bittrex to get the selected tickers
	Then it compares to the given numbers from Golix
	Finaly it calculates the best transaction path for the user.
"""

import pandas as pd
import BittrexInterface as bx

def getActualTickerValues(market):
	data = bx.getTicker(market)
	return pd.DataFrame([
		[market,data["Bid"],data["Ask"]]],
		columns = ["Market","Bid","Ask"])

def getTikersAsArray():
	bitcoin = getActualTickerValues("USDT-BTC")
	dash = getActualTickerValues("USDT-DASH")
	litecoin = getActualTickerValues("USDT-LTC")
	cash = getActualTickerValues("USDT-BCC")
	gold = getActualTickerValues("USDT-BTG")
	etherium = getActualTickerValues("USDT-ETH")

	bittrex = bitcoin
	bittrex = bittrex.append(dash,ignore_index=True)
	bittrex = bittrex.append(litecoin,ignore_index=True)
	bittrex = bittrex.append(cash,ignore_index=True)
	bittrex = bittrex.append(gold,ignore_index=True)
	bittrex = bittrex.append(etherium,ignore_index=True)
	return bittrex

def getManualValues():
	golix = pd.DataFrame([
		["BTC-USD",18000,18390],
		["DASH-USD",1210,1350],
		["LTC-USD",155,166],
		["BCC-USD",2220,2440],
		["BTG-USD",100000,100000],
		["ETH-USD",100000,100000]]
		,columns = ["Market","Bid","Ask"])
	return golix

def compare(a, b):
	minComp = 10
	maxComp = 0

	coinToSend="BTC-USD"
	priceToSend=10000
	
	"""for x in range(len(a.index)):
		sendWinPercentage = (b[x][Ask]-a[x][Bid]) / a[x][Bid]
		print(sendWinPercentage)
		if (sendWinPercentage > maxComp):
			maxComp = sendWinPercentage
			coinToSend = a[x][Market]
			priceToSend = a[x][Bid]"""
	
	coinToBring=a[1][1]
	priceToBring=10000

	"""for x in range(len(a.index)):
		bringWinPercentage = (b[x][Ask]-a[x][Bid]) / a[x][Bid]
		print(bringWinPercentage)
		if (bringWinPercentage < minComp):
			minComp = bringWinPercentage
			coinToBring = a[x][Market]
			priceToBring = a[x][Bid]"""

	return "Send "+coinToSend+" at: "+str(priceToSend)+"\nBring "+coinToBring+" at: "+str(priceToBring)

def main():
	print("\n\n---------------------")
	print("And so it begins...\n\n\n")
	
	bittrex = getTikersAsArray();
	golix = getManualValues();
	result = compare(bittrex,golix);
	print(result)

if __name__ == '__main__':
	main()
else:
	print("Importing module {} may not be useful".format(__name__))