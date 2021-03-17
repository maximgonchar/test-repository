import unittest
from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link0 = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome('/Users/m.gonchar/Downloads/chromedriver')
        browser.get(link0)
        element1 = browser.find_element_by_xpath('//input[@class="form-control first"][@placeholder="Input your first name"]')
        element1.send_keys("Test")
        element2 = browser.find_element_by_xpath('//input[@class="form-control second"][@placeholder="Input your last name"]')
        element2.send_keys("QA")
        element3 = browser.find_element_by_xpath('//input[@class="form-control third"][@placeholder="Input your email"]')
        element3.send_keys("tel@net.qa")
        element4 = browser.find_element_by_xpath('//input[@class="form-control first"][@placeholder="Input your phone:"]')
        element4.send_keys("495-456-654-32")
        element5 = browser.find_element_by_xpath('//input[@class="form-control second"][@placeholder="Input your address:"]')
        element5.send_keys("Moscow")
        button = browser.find_element_by_xpath('//button[@type="submit"]')
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        time.sleep(1)
        browser.quit()
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome('/Users/m.gonchar/Downloads/chromedriver')
        browser.get(link)
        element1 = browser.find_element_by_xpath('//input[@class="form-control first"][@placeholder="Input your first name"]')
        element1.send_keys("Test")
        element2 = browser.find_element_by_xpath('//input[@class="form-control second"][@placeholder="Input your last name"]')
        element2.send_keys("QA")
        element3 = browser.find_element_by_xpath('//input[@class="form-control third"][@placeholder="Input your email"]')
        element3.send_keys("tel@net.qa")
        element4 = browser.find_element_by_xpath('//input[@class="form-control first"][@placeholder="Input your phone:"]')
        element4.send_keys("495-456-654-32")
        element5 = browser.find_element_by_xpath('//input[@class="form-control second"][@placeholder="Input your address:"]')
        element5.send_keys("Moscow")
        button = browser.find_element_by_xpath('//button[@type="submit"]')
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        time.sleep(1)
        browser.quit()

if __name__ == "__main__":
    unittest.main()