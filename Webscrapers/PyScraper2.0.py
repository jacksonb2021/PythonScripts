"""
The following program was made as a test build of a webscraper made with the selenium webdriver

This program is PROOF OF CONCEPT. Do not run anywhere where piracy is illegal. I do not condone piracy

You need a .CRX copy of the adblockplus chrome extension
https://chromewebstore.google.com/detail/crx-extractordownloader/ajkhmmldknmfjnmeedkbkkojgobmljda
use this tool to download the extension, then name it adblockplus.crx
"""

import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from pynput.keyboard import Key, Controller

keyboard = Controller()


games = os.path.dirname(os.path.realpath(__file__))+'/games.txt'
try:
    file = open(games, 'r')
    print("games.txt found... reading games\n")
except FileNotFoundError:
    print("games.txt was not found. creating...\n")
    gamename = input("Enter the name of the game you want to download. Click enter with no text when done\n")
    the_string = gamename+"\n"
    while gamename != "":
        gamename = input(f"added {gamename}. Enter another game, or enter to end input\n")
        the_string += gamename+"\n"
    file = open(games,'w')
    file.write(the_string)
    file.close()
    file = open(games,'r')

lines = file.readlines()
options = webdriver.ChromeOptions()
ublockpath = os.path.dirname(os.path.realpath(__file__)) + "/adblockplus.crx"

options.add_extension(ublockpath)
browser = webdriver.Chrome(options=options)
# wait for adblock to load
browser.get("https://google.com")
time.sleep(3)
browser.switch_to.window(browser.window_handles[0])
for i in lines:
    browser.get("https://thepiratebay.org/index.html")
    gamename = i.strip()
    searchbox = browser.find_element(By.TAG_NAME, 'input')
    searchbox.send_keys(gamename)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[0])
    table = browser.find_elements(By.CLASS_NAME, 'list-entry')
    correct = None
    for elem in table:
        browser.switch_to.window(browser.window_handles[0])
        user = elem.find_element(By.CSS_SELECTOR, ".list-item.item-user")
        try:
            name = user.find_element(By.TAG_NAME, 'a')
        except NoSuchElementException:
            continue
        if name.text == 'dauphong':
            correct = elem
            break

    if correct is None:
        print(f'could not find: {i}\n')
        continue
    browser.switch_to.window(browser.window_handles[0])
    download = elem.find_element(By.CLASS_NAME, 'item-icons').find_element(By.TAG_NAME, 'a')
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
    #todo switch back to selenium chromium window- can sometimes not be in corrrect window
file.close()
