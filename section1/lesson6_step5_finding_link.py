from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link2 = browser.find_element(By.LINK_TEXT, str(
        math.ceil(math.pow(math.pi, math.e)*10000)))
    link2.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ilya")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Krivoshein")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Tomsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    driver.close()
    time.sleep(2)
    driver.quit()

# не забываем оставить пустую строку в конце файла
