"""
	Author: Luis_C-137
	Bittrex API interface
"""

import requests

ticker = 'https://bittrex.com/api/v1.1/public/getticker?market='
markets = 'https://bittrex.com/api/v1.1/public/getmarkets'

def getJSON(petition):
	return requests.get(petition).json()

def getBittrexJSON(petition):
	data = getJSON(petition)
	if (data["success"] == True):
		return data["result"]
	else:
		print("Failed to get JSON because: " + data["message"])
		return data['message']

def getTicker(market):
	return getBittrexJSON(ticker + market)

def printTicker(market):
	data = getTicker(market)
	print(market,"\t Bid:",data["Bid"],"\t Ask:",data["Ask"],"\t Last:",data["Last"])

def printMarkets():
	data = getBittrexJSON(markets)	

	for market in data:
		print(market["MarketName"],"\t",market["MarketCurrencyLong"])

def main():
	print("\n\n---------------------")
	print("And so it begins...\n\n\n")

	printMarkets()
	printTicker("USDT-BTC")
	

if __name__ == '__main__':
	main()
else:
	print("You are mporting module {}".format(__name__))