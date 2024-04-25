import os
from dotenv import load_dotenv

if not load_dotenv():
    print('Failed to load .env file... Please check')

bind = os.getenv('bind')
workers = os.getenv('workers')
