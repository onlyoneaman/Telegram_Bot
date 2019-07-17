import requests                 # for making HTTP requests
import json                     # library for handling JSON data
import time                     # module for sleep operation
import conf

def send_telegram_message(message):
	'''Sends message via telegram'''
	telegram_url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
	data = {
		"chat_id": conf.telegram_BTCchat_id,
		"text": message
	}
	try:
		response = requests.request(
			"POST",
			telegram_url,
			params=data
			)
		print("This is the Telegram response")
		print(response.text)
		telegram_data = json.loads(response.text)
		return(telegram_data["ok"])
	except Exception as e:
		print("Error")
		print(e)
		return(False)

#api-key for INR of BTC
url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=INR"


while(True):
	btc_response=requests.get(url)
	datatxt = btc_response.text
	parsed = json.loads(datatxt)
	price = parsed["INR"]
	message = "INR Price of BTC :" + str(price)
	telegram_status = send_telegram_message(message)
	print("Telegram Status:",telegram_status)
	time.sleep(600)