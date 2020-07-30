import time
import math
import pytest
from selenium import webdriver

#answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    link = f"{link}"
    browser.get(link)
    browser.implicitly_wait(10)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_tag_name("textarea").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(3)
    hint = browser.find_element_by_class_name("smart-hints__hint")
    print(str(hint.text))
    time.sleep(1)
    assert hint.text == "Correct!", "Неверный ответ"



