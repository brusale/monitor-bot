from telegram.ext import Updater, CommandHandler, MessageHandler
import os

class MonitorBot:

	def __init__(self, TOKEN, CHAT_ID, URL):
		self.TOKEN = TOKEN
		self.CHAT_ID = CHAT_ID
		self.url = URL

	def check_url(self, response):
		if response not in ['yes', 'no']:
			print(">>> Please answer yes or no")
			response = update.message.text.lower()
			check_url(response)
		elif response == 'yes':
			return True
		else:
			return False
		
	
	
