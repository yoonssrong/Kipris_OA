from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import time
import pandas as pd
import re
import os

# 랜덤으로 유저 에이전트 생성
ua = UserAgent(verify_ssl=False)
userAgent = ua.random
print(userAgent)

# 크롬 드라이버 옵션
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")
options.add_argument('user-agent={}'.format(userAgent))

folderPath = os.path.dirname(os.path.realpath(__file__))
packed_extension_path = folderPath + '/extensions/mpbjkejclgfgadiemmefgebjfooflfhl.crx'
options.add_extension(packed_extension_path)

# 수집 대상 url
url = 'https://www.tmdn.org/tmview/#/tmview/results?page=1&pageSize=30&criteria=C&offices=AT,BG,BX,CY,CZ,DE,DK,EE,ES,FI,FR,GB,GR,HR,HU,IE,IT,LT,LV,MT,PL,PT,RO,SE,SI,SK,EM,WO&territories=EU&viennaCode=03.01.08&viennaCodeVersion=wipo'
driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
driver.get(url)

time.sleep(30)

html = driver.page_source
html_bs = bs(html, 'html.parser')

downButton = driver.find_elements_by_xpath('//*[@id="main"]/div/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/button')
downButton[0].click()

xlsButton = driver.find_elements_by_class_name('kqaacT')
xlsButton[1].click()

rangeValue = driver.find_elements_by_class_name('gpmTzN')
rangeValue[0].send_keys(Keys.CONTROL + "a")
rangeValue[0].send_keys('2')
rangeValue[1].send_keys(Keys.CONTROL + "a")
rangeValue[1].send_keys('100')

viennaCheck = driver.find_element_by_css_selector('body > div.ReactModalPortal > div > div > div > div.sc-AxiKw.bwtSwc.sc-fzplgP.kZdFWj > div > div:nth-child(3) > div.sc-AxiKw.bwtSwc > div:nth-child(16) > div > label > input[type=checkbox]')
viennaCheck.click()

submitButton = driver.find_element_by_css_selector('body > div.ReactModalPortal > div > div > div > div.sc-AxiKw.bwtSwc.sc-fznzqM.iyQblJ > div.sc-AxiKw.bbPiOk > button.sc-fznKkj.hJhEgn')
submitButton.send_keys(Keys.ENTER)

# recaptcha 처리
mainwindow = driver.current_window_handle
frame = driver.find_element_by_tag_name("iframe")
print(frame)
driver.switch_to.frame(frame)
driver.find_element_by_id("recaptcha-anchor").click()
driver.switch_to.window(mainwindow)
