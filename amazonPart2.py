# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:09:14 2020

@author: shruti
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logindata

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver', chrome_options=options)
action = ActionChains(driver)
time.sleep(1)


driver.get('http://www.amazon.in')
time.sleep(3)
 
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)
 
secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(logindata.USERNAME)
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(logindata.PASSWORD)
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys('sunglasses')
search.send_keys(Keys.ENTER)
time.sleep(3)

sortby = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[1]')
sortby.click()
time.sleep(3)

low = driver.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
low.click()
time.sleep(3)

elem = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/div[2]/div/span/a/div')
elem.click()
time.sleep(3)


driver.switch_to_window(driver.window_handles[1]) ##used to switche between tabs

addtocart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
addtocart.click()
time.sleep(3)

proceed = driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')
proceed.click()
time.sleep(3)

deliver = driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a')
deliver.click()
time.sleep(3)
