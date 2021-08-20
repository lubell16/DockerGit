from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver=webdriver.Chrome('./chromedriver', options=options)

driver.get('https://selenium-python.readthedocs.io/getting-started.html')

driver.save_screenshot('https://python.org')