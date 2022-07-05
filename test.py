from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.localhost:8000')
assert browser.page_source.find('DEBUG')
browser.close()