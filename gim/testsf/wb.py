import webbrowser,requests
# from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Unmanned_spacecraft'
url2 = 'http://www.google.co.jp/trends/explore?q=Unmanned_ground_vehicle'
# r = requests.get(url2)
# r.encoding = 'utf-8'
# doc = r.text
# print doc
# pagesoup = BeautifulSoup(doc, 'lxml')
# print pagesoup.find(id='mw-content-text')

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get(url)
driver.maximize_window()
# driver.find_element_by_id('mw-content-text')
driver.save_screenshot('screenshot.png')