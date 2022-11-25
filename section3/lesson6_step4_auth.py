from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

import config
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()

def test_authorization(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    browser.implicitly_wait(5)

    browser.find_element(By.ID, "ember32").click()
    browser.find_element(By.ID, "id_login_email").send_keys(config.stepik_secret_login)
    browser.find_element(By.ID, "id_login_password").send_keys(config.stepik_secret_password)
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

    browser.implicitly_wait(5)

    assert browser.find_element(By.CLASS_NAME, "navbar__profile-img")