from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.dcard.tw/service/api/v2/globalPaging/page?pageKey=dadcd689-0b77-4cf6-8c08-46aaa6e30afc&enrich=true&platform=web&noWidget=true'

options = Options()
latestchromedriver = ChromeDriverManager().install()
#set options
driver = webdriver.Chrome(driver_executable_path=latestchromedriver, options=options)
driver.get(url)