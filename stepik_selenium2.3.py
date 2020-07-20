from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(executable_path= r'C:\chromedriver.exe')
    browser.get(link)
    """number1 = browser.find_element_by_id('num1')
    x = number1.text
    number2 = browser.find_element_by_id('num2')
    y = number2.text
    answer = int(x) + int(y)
    print(answer)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(answer))  # ищем элемент с текстом "Python"
    button = browser.find_element_by_class_name('btn-default')
    button.click()"""
    button = browser.find_element_by_class_name('btn-primary')
    button.click()
    """confirm = browser.switch_to.alert
    confirm.accept()"""
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    number = browser.find_element_by_id('input_value')
    x = number.text
    print(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))
    """checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radButton = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radButton)
    radButton.click()"""
    button1 = browser.find_element_by_class_name('btn-primary')
    button1.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()