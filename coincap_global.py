import requests
import json

local_currency = "USD"
local_symbol = "$"
api_key = '1e26231a-2422-4a1a-b92e-5a99e56b71c2'
headers = {'X-CMC_PRO_API_KEY':api_key}

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency


global_url2 = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

request = requests.get(global_url2,headers=headers)

results = request.json()
print(json.dumps(results,sort_keys=True,indent=4))



def crypto(results):
	data = results['data']
	for currency in data:
		name = currency['name']
		symbol = currency['symbol']
		price = currency['quote'][local_currency]['price']
		percent_change_24h = currency['quote'][local_currency]['percent_change_24h']
		market_cap = currency['quote'][local_currency]['market_cap']
		price = round(price,2)
		percent_change_24h = round(percent_change_24h,2)
		market_cap = round(market_cap,2)
		price_string = local_symbol + '{:,}'.format(price)
		percent_change_24h_string = local_symbol + '{:,}'.format(percent_change_24h)
		market_cap_string = local_symbol + '{:,}'.format(market_cap)
		print(name + '(' + symbol + ')')
		print("Price: " +price_string)
		print("24h Change: " +percent_change_24h_string)
		print('Market cap: ' + market_cap_string)
		print()


def general_data(results):

	data = results['data']
	btc_dominance = data['btc_dominance']
	eth_dominance = data['eth_dominance']
	total_market_cap = data["quote"][local_currency]["total_market_cap"]
	total_volume_24h = data["quote"][local_currency]["total_volume_24h"]
	total_market_cap = round(total_market_cap,2)
	total_volume_24h = round(total_volume_24h,2)

	btc_dominance = round(btc_dominance,2)
	eth_dominance = round(eth_dominance,2)

	total_market_cap_string = local_symbol + '{:,}'.format(total_market_cap)
	total_volume_24h_string = local_symbol + '{:,}'.format(total_volume_24h)

	print()
	print("The global market cap for all crypto is " + total_market_cap_string + " and the global 24h volume is " + total_volume_24h_string)
	print()
	print("Bitcoin dominance is " +str(btc_dominance) + "% and Eth dominance is " + str(eth_dominance) + '%')

crypto(results)