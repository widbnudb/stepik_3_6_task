from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_button(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".add-to-basket .btn")
    assert button is not None


