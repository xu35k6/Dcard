from asyncore import write
import pandas as pd
import requests
import re
from fake_useragent import UserAgent
import random
import time
import openpyxl
ua = UserAgent()

url = "https://www.dcard.tw/service/api/v2/forums/talk/posts?popular=true&limit=30&before=235999153"
r = requests.get(url
                , headers = {
    "user_agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
  }
               )
print(r.status_code)