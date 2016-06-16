# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHANNEL_NAME = os.environ.get('CHANNEL_NAME', '@HHSearcherBot')
SCAN_DELAY = os.environ.get('SCAN_DELAY', 60)
