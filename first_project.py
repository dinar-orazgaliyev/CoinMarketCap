import os
import csv 
import json
import requests
from prettytable import PrettyTable
from colorama import Fore, Back, Style

local_currency = "USD"
local_symbol = "$"
api_key = '1e26231a-2422-4a1a-b92e-5a99e56b71c2'
headers = {'X-CMC_PRO_API_KEY':api_key}
base_url = 'https://pro-api.coinmarketcap.com'
table = PrettyTable(['Asset', 'Amount Owned', 'Value', 'Price', '1h','24h','7d'])

def dum():
	portfolio_value = 0.00
	
	with open("my_portfolio.csv","r") as f:
		lines = csv.reader(f)
		for line in lines:
			if '\ufeff' in line[0]:
				line[0] = line[0][1:].upper()
			else:
				line[0] = line[0].upper()
			amount = line[1]
		symbol = line[0]
		amount = line[1]
		quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol

		request = requests.get(quote_url,headers=headers)
		results = request.json()

		#print(json.dumps(results,sort_keys=True, indent=4))

		currency = results['data'][symbol]
		name = currency['name']
		quote = currency['quote'][local_currency]
		hour_change = round(quote['percent_change_1h'],1)
		day_change = round(quote['percent_change_24h'],1)
		week_change = round(quote['percent_change_7d'],1)
		price = quote['price']
		value = float(price) * float(amount)
		portfolio_value += value 
		price_string = '{:,}'.format(round(price,2))
		value_string = '{:,}'.format(round(value,2))
		if hour_change > 0:
			hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
		else:
			hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

		if day_change > 0:
			day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
		else:
			day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

		if week_change > 0:
			week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
		else:
			week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

		price_string = '{:,}'.format(round(price,2))
		value_string = '{:,}'.format(round(value,2))

		table.add_row([name + ' (' + symbol + ')',
					amount,
					local_symbol + value_string,
					local_symbol + price_string,
					str(hour_change),
					str(day_change),
					str(week_change)])


	print(table)
	print()
	portfolio_value_string = '{:,}'.format(round(portfolio_value,2))
	print('Total Portfolio Value: ' + Back.GREEN + local_symbol + portfolio_value_string + Style.RESET_ALL)
	print()
dum()



