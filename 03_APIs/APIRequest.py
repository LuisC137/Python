"""
	Author: Luis_C-137
	This API comunicates with bittrex
"""

import requests

ticker = 'https://bittrex.com/api/v1.1/public/getticker?market='
markets = 'https://bittrex.com/api/v1.1/public/getmarkets'

def getJSON(petition):
	return requests.get(petition).json()

def getMarkets():
	return getJSON(markets)

def getActiveMarkets():
	data = getMarkets()
	active = []
	for m in data:
		if (m['IsActive']):
			active.add(m)
	return active

def printTicker(market):
	data = getJSON(ticker + market["MarketName"])
	print(market["MarketCurrencyLong"])
	if (data["success"] == True):
		result = data["result"]
		print("\tBid:\t " + '{:0.8f}'.format(result["Bid"]))
		print("\tAsk:\t " + '{:0.8f}'.format(result["Ask"]))
		print("\tLast:\t " + '{:0.8f}'.format(result["Last"]))
	else:
		print("Failed to get JSON because: " + data["message"])

def main():
	print("\n\n---------------------")
	print("And so it begins...\n\n\n")

	marketList = getActiveMarkets()

	for market in marketList['result']:
		printTicker(market)
	

if __name__ == '__main__':
	main()
else:
	print("Importing module {} may not be useful".format(__name__))
