import logging
import tomllib
import argparse

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		    level=logging.INFO)

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="TOML file for bot token and server url")
args = parser.parse_args()

def parse_config(config_file):
	with open(config_file, "rb") as f:
		config = tomllib.load(f)

	## get config for telegram bot
	TOKEN = config["telegram-bot"]["API_TOKEN"]
	CHAT_ID = config["telegram-bot"]["CHAT_ID"]
	BOT_NAME = config["telegram-bot"]["NAME"]

	## get config for target server
	TARGET_URL = config["server"]["url"]

	return TOKEN, CHAT_ID, TARGET_URL

def main(args):
	TARGET_URL, CHAT_ID, TARGET_URL = parse_config(args.config)



if __name__ == "__main__":
	main(args)
	