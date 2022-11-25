from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

import config
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_authorization(browser, link):
    link = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")))
    browser.find_element(By.CSS_SELECTOR,".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
    browser.find_element(By.ID, "id_login_email").send_keys(config.stepik_secret_login)
    browser.find_element(By.ID, "id_login_password").send_keys(config.stepik_secret_password)
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR,".sign-form__btn.button_with-loader").click()
    time.sleep(2)

    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR,".textarea").send_keys(str(answer))

    browser.find_element(By.CSS_SELECTOR,".submit-submission").click()
    browser.implicitly_wait(10)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

    assert text == "Correct!", f"Wrong answer: {text}"

    
