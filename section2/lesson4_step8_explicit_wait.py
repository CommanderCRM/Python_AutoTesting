from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ждем пока цена будет равна 100 долларам и жмем
    button = browser.find_element(By.ID,"book")
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

    # автоматическое получение численного ответа
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    alert_number = float(alert_text.split(': ')[-1])
    print(alert_number)
    
finally:
    time.sleep(10)
    browser.quit()