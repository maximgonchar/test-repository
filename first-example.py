from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://yandex.ru/")
time.sleep(3)
browser.quit()