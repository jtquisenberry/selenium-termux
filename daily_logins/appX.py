# Based on
# https://github.com/mozilla/geckodriver/releases
# https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
# https://www.quora.com/How-can-I-write-a-Python-script-to-open-a-webpage-and-login-to-a-website-in-the-background-automatically-as-soon-as-I-connect-to-LAN

from selenium import webdriver
import time
from datetime import datetime
import os
import sys
import json

now = datetime.now()
timestamp = str(now).replace(' ', '_').replace(':', '-').replace('.', '-')
os.chdir(os.path.dirname(__file__))

screenshot_dir = r'E:\Development\private\daily_logins'

with open(r"E:\Development\private\daily_logins.json") as f:
    data = json.load(f)
    dummy_breakpoint = 1


def logon_gamefaqs():
    browser = webdriver.Firefox(executable_path=r'./geckodriver.exe')
    print("Logging into stackoverflow.com")
    # browser = webdriver.Firefox()

    username = data['gamefaqs']['username']
    password = data['gamefaqs']['password']

    try:
        browser.get('https://gamefaqs.gamespot.com/')
        login_link = browser.find_element_by_link_text('Log In')
        login_link.click()
        time.sleep(2)  # seconds

        username_box = browser.find_element_by_id('login_email')
        username_box.send_keys(username)
        password_box = browser.find_element_by_id('login_password')
        password_box.send_keys(password)
        login_button = browser.find_element_by_id('login_submit')
        login_button.click()
        time.sleep(1)
        browser.get_screenshot_as_file(screenshot_dir + '/GameFAQs' + timestamp + '.png')
        time.sleep(3)
    except Exception as e:
        print("An error occurred while trying to access GameFAQs", e)
    finally:
        browser.close()
        print('DONE with GameFAQs')

def logon_stackoverflow():
    browser = webdriver.Firefox(executable_path=r'./geckodriver.exe')
    print("Logging into stackoverflow.com")

    username = data['stackoverflow']['username']
    password = data['stackoverflow']['password']

    try:
        browser.get("https://stackoverflow.com")
        browser.find_element_by_link_text("Log in").click()

        browser.find_element_by_id("email").send_keys(username)
        browser.find_element_by_id("password").send_keys(password)
        browser.find_element_by_id("submit-button").submit()
        time.sleep(3)

        browser.find_element_by_class_name("my-profile").click()
        time.sleep(3)

        browser.get_screenshot_as_file(screenshot_dir + '/stackoverflow' + timestamp + '.png')
        time.sleep(3)

    except Exception as e:
        print("An error occurred while trying to access stackoverflow.com!", e)
    finally:
        browser.close()
        print("DONE with StackOverflow")


if __name__ == '__main__':
    logon_gamefaqs()
    logon_stackoverflow()
