from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://yandex.ru/")
time.sleep(2)
browser.quit()