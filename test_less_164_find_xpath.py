
from selenium import webdriver
import time
link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome('/Users/m.gonchar/Downloads/chromedriver')
    browser.get(link)
    element1 = browser.find_element_by_xpath('//input[@name="first_name"]')
    element1.send_keys("Макс")
    element2 = browser.find_element_by_xpath('//input[@name="last_name"]')
    element2.send_keys("QA")
    element3 = browser.find_element_by_xpath('//input[@class="form-control city"]')
    element3.send_keys("Moscow")
    element4 = browser.find_element_by_xpath('//input[@id="country"]')
    element4.send_keys("RF")

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
except:
    time.sleep(10)
    browser.quit()