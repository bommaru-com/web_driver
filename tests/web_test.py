import sys
from web_driver import WebDriver, WebDriverError


def main(connect_type):
    try:
        driver = None
        browser = None
        if connect_type == 'chromedriver':
            browser = WebDriver(driver_path='./chromedriver')
        elif connect_type == 'remote':
            browser = WebDriver(remote_url='http://220.86.210.44:4444')
        driver = browser.connect()
        driver.get('http://www.naver.com')
        print('web site title is %s' % driver.title)
        browser.quit()
    except Exception as e:
        print(type(e), str(e))
        if browser is not None:
            browser.quit()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('option: chromedriver or remote')