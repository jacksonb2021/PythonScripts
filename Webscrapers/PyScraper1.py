import time, keyboard, pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from pynput.keyboard import Key, Controller
keyboard = Controller()

options = webdriver.ChromeOptions()
ublockpath = os.path.dirname(os.path.realpath(__file__))+"/ublock.crx"

options.add_extension(ublockpath)

browser = webdriver.Chrome(options=options)
file = open("games.txt",'r')
lines = file.readlines()
for i in lines:


    browser.get("https://pcgamestorrents.com")


    #time.sleep(2)
    gamename = i.strip()
    searchbar = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/main/div/div/aside/div[1]/div[1]/div/form/input')
    searchbar.send_keys(gamename)
    searchbar.send_keys(Keys.RETURN)
    #time.sleep(2)
    allresults = browser.find_element(By.CLASS_NAME,"uk-link-reset")
    allresults.click()
    browser.switch_to.window(browser.window_handles[0])

    #TODO: find the class of this shit
    tordownload = browser.find_element(By.CSS_SELECTOR,'.uk-card.uk-card-body.uk-card-default.uk-card-hover').find_element(By.TAG_NAME,"a")
    #tordownload = browser.find_element(By.XPATH, '//*[@id="post-309731"]/div[2]/p[18]/a')
    tordownload.click()
    time.sleep(8)
    browser.switch_to.window(browser.window_handles[0])
    downloadbutton = browser.find_element(By.ID,'nut')
    downloadbutton.click()

    time.sleep(1)

    keyboard.press(Key.left)
    keyboard.release(Key.left)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # tordownload[0].click()
    # time.sleep(5)
