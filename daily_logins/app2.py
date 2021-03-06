import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def do_capture():

    print("XXXXXXXX")
    print("HEADLESS", os.path.abspath('./bin/headless-chromium'))
    print("CHROMEDRIVER", os.path.abspath('./bin/chromedriver'))

    options = Options()
    options.binary_location = './bin/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('./bin/chromedriver', service_log_path='./bin', chrome_options=options)

    driver.get('https://www.google.com/')
    body = f"Headless Chrome Initialized, Page title: {driver.title}"

    driver.close();
    driver.quit();

    return {
        "statusCode": 200,
        "body": body
    }

if __name__ == '__main__':
    do_capture()