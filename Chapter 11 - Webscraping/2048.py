#! usr/bin/env python3
# 2048.py - Launches the 2048 game and plays it automatically

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open browser
browser = webdriver.Firefox()
#open webpage
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

#define inputs
def urdl():
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)

#input loop
def run(times):

    button = browser.find_element_by_class_name('retry-button')
    while button.is_displayed() == False:
        urdl()
        
#restart
    button.click()

    if times > 0:
        run(times - 1)

run(5)
