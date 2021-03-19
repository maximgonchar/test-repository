import math

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "https://stepik.org/lesson/236897/step/1"

@pytest.fixture
def browser_ex():
    print("\nstart browser")
    browser = webdriver.Chrome()
    yield browser
    print("\nclose browser")
    browser.quit()



# def test_try(browser_ex):
#     browser_ex.get(link)
#     answer = math.log(int(time.time()))
#     browser_ex.implicitly_wait(5)
#     input_answer = browser_ex.find_element_by_xpath('//div[@data-state="no_submission"]/textarea')
#     input_answer.send_keys(str(answer))
#     button = browser_ex.find_element_by_class_name('submit-submission')
#     button.click()
#     res = WebDriverWait(browser_ex, 5).until(
#         EC.visibility_of_element_located((By.XPATH, '//pre'))
#     )
#     assert res.text == 'Correct!', "Пойманное слово: " + res.text
