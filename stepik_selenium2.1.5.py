from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #link = "http://suninjuly.github.io/math.html"
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(executable_path= r'C:\chromedriver.exe')
    browser.get(link)
    """number = browser.find_element_by_id('input_value')
    x = number.text
    print(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radButton = browser.find_element_by_id('robotsRule')
    radButton.click()
    button = browser.find_element_by_class_name('btn-default')
    button.click()"""
    number = browser.find_element_by_id('treasure')
    x = number.get_attribute('valuex')
    print(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radButton = browser.find_element_by_id('robotsRule')
    radButton.click()
    button = browser.find_element_by_class_name('btn-default')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()