import sys
sys.path.append('../')
import unittest
import tempfile
import argparse
import os
from unittest.mock import patch
from main import create_parser, parse_config
import toml

class TestConfigParser(unittest.TestCase):

	def test_create_parser(self):
		parser = create_parser()
		self.assertIsInstance(parser, argparse.ArgumentParser)

	def test_parse_config(self):
		with tempfile.TemporaryDirectory(dir=".") as tmp:
			path = os.path.join(tmp)
			print(path)
			data = {
				"telegram-bot": {
					"API_TOKEN": "token1234",
					"CHAT_ID": "chat1234",
					"NAME": "TestBot"
				},
				"server": {
					"url": "https://example.com"
				}
			
			}

			tmp_file = path+"/test_config.toml"
	
			with open(tmp_file, "w") as test_toml:
				toml.dump(data, test_toml)

			result = parse_config(tmp_file)
			self.assertEqual(result, ('token1234', 'chat1234', 'TestBot', 'https://example.com'))		

	def tearDown(self):
		 patch.stopall()

if __name__ == "__main__":
	unittest.main()
