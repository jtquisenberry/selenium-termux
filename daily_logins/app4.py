from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def hello():
    print("HHHHHHHH")

    options = Options()
    options.binary_location = '/bin/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/bin/chromedriver',chrome_options=options)

    driver.get('https://www.google.com/')
    print(driver.page_source[:250])
    body = f"Headless Chrome Initialized, Page title: {driver.title}"

    driver.close();
    driver.quit();

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

if __name__ == '__main__':
    hello()