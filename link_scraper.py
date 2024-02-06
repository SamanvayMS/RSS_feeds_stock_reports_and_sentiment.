import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://www.moneycontrol.com/india/newsarticle/rssfeeds/rssfeeds.php'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

# Finding all <a> tags in the HTML content
links = soup.find_all('a')

# Extracting the href attribute from each <a> tag
rss_links = [link for link in links if 'rss' in link]

with open('rss_links.txt', 'w') as f:
    for link in rss_links:
        f.write(link + '\n')