import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.get('https://petfriends.skillfactory.ru/login')
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    yield driver

    driver.quit()

