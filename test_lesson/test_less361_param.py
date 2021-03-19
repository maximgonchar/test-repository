import math
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1]"]

total_answer = ''

@pytest.fixture(scope="function")
def browser_ex():
    print("\nstart browser for test..")
    browser_ex = webdriver.Chrome()
    yield browser_ex
    print("\nquit browser..")
    browser_ex.quit()
    print("YYYYYYYYY")
    print(total_answer)

@pytest.mark.parametrize('link', links)


def test_nlo(browser_ex, link):

    global total_answer
    browser_ex.implicitly_wait(5)
    browser_ex.get(link)
    answer = str(math.log(int(time.time())))
    wait = WebDriverWait(browser_ex, 5)
    input_answer = browser_ex.find_element_by_xpath('//div[@data-state="no_submission"]/textarea')
    input_answer.send_keys(answer)
    button = browser_ex.find_element_by_class_name('submit-submission')
    button.click()
    res = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//pre'))
    )
    text_check = res.text
    if "Correct!" not in text_check:
        total_answer += text_check
    assert text_check == 'Correct!', "NLO found"


