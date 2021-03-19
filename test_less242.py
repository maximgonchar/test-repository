import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from test_suites.Platform.Stepic.test_less21 import calc
from test_suites.Platform.Stepic.test_less231 import Locat
link = 'http://suninjuly.github.io/explicit_wait2.html'
#price = By.ID, 'price'


@pytest.fixture(scope="function")
def browser(multi_browser):
    multi_browser.get(link)
    yield multi_browser

class TestNewWindow:
    def test_new_win(self, browser):
        #priceq = browser.find_element_by_xpath('//h5[@id="price"]')
        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
        button = browser.find_element_by_xpath('//button[@id="book"]')
        button.click()
        x_elem = browser.find_element_by_xpath('//span[@id="input_value"]')
        x = x_elem.text
        y = calc(x)
        input_elem = browser.find_element_by_xpath('//input[@id="answer"]')
        input_elem.send_keys(y)
        submit = browser.find_element_by_xpath('//*[@type="submit"]')
        submit.click()
        time.sleep(10)
