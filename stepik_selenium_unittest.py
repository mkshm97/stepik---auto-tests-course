from selenium import webdriver
import time
import os
import unittest
import pytest

class stepik_selenium_unittest(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('input[required].first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input[required].second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input[required].third')
        input3.send_keys("mkshm@ya.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        result = browser.find_element_by_tag_name('h1')
        print(result.text)

        # Проверяем, что смогли зарегистрироваться
        self.assertEqual("Congratulations! You have successfully registered!", result.text, "Should be successful registration")
        # ждем загрузки страницы
        """time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text"""
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('input[required].first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input[required].second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input[required].third')
        input3.send_keys("mkshm@ya.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        result = browser.find_element_by_tag_name('h1')
        print(result.text)
        # Проверяем, что смогли зарегистрироваться
        self.assertEqual("Congratulations! You have successfully registered!", result.text, "Should be successful registration")
        # ждем загрузки страницы
        """time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text"""
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()