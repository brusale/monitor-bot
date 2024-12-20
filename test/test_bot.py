import sys
sys.path.append("./")
import unittest
from unittest.mock import patch
from src.MonitorBot import MonitorBot

token = "token"
chat_id = "chat_id"
url = "https://url.com"

class TestMonitorBot(unittest.TestCase):
	def test_bot_type(self):
		bot = MonitorBot(token, chat_id, url)
		self.assertIsInstance(bot, MonitorBot)

	def test_check_url(self):
		bot = MonitorBot(token, chat_id, url)
		
		self.assertEqual(bot.check_url('yes'), True)	
		self.assertEqual(bot.check_url('no'), False)


	def tearDown(self):
		patch.stopall()

if __name__ == "__main__":
	unittest.main()
