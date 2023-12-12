import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from pynput.keyboard import Key, Controller
keyboard = Controller()

#comment the following lines out if you do not have the adblock
options = webdriver.ChromeOptions()
ublockpath = os.path.dirname(os.path.realpath(__file__))+"/adblockplus.crx"

options.add_extension(ublockpath)
browser = webdriver.Chrome(options=options)
file = open("games.txt",'r')
lines = file.readlines()


# wait for adblock to load
browser.get("https://google.com")
time.sleep(3)
browser.switch_to.window(browser.window_handles[0])
for i in lines:
    browser.get("https://thepiratebay.org/index.html")
    gamename = i.strip()
    searchbox = browser.find_element(By.TAG_NAME,'input')
    searchbox.send_keys(gamename)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[0])
    table = browser.find_elements(By.CLASS_NAME,'list-entry')
    correct = None
    for elem in table:
        browser.switch_to.window(browser.window_handles[0])
        user = elem.find_element(By.CSS_SELECTOR,".list-item.item-user")
        try:
            name = user.find_element(By.TAG_NAME,'a')
        except NoSuchElementException:
            continue
        if name.text == 'dauphong':
            correct = elem
            break

    if correct is None:
        print(f'could not find: {i}\n')
        continue
    browser.switch_to.window(browser.window_handles[0])
    download = elem.find_element(By.CLASS_NAME, 'item-icons').find_element(By.TAG_NAME,'a')
    download.click()
    time.sleep(1)

    keyboard.press(Key.left)
    keyboard.release(Key.left)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)





