import time
from web_driver import WebDriver, WebDriverError
from bs4 import BeautifulSoup

try:
    # browser = WebDriver(
    #     session_url='http://220.86.210.44:4444'
    # )
    browser = WebDriver(
        driver_path='./chromedriver',
        remote_url='http://220.86.210.44:4444'
    )
    driver = browser.connect()
    # print(driver)
    time.sleep(5)
    driver.get('http://www.naver.com')
    print(driver.title)

    browser.disconnect()
except Exception as e:
    print(str(e))