import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_all_pets(driver):
    driver.find_element(By.ID, 'email').send_keys('stanislav-irk@bk.ru')
    driver.find_element(By.ID, 'pass').send_keys('Taisia-28.11')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(driver, 10)
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.get('https://petfriends.skillfactory.ru/my_pets')

    all_my_pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr')

    driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr/th/img')

    # проверяем что список своих питомцев не пуст
    assert len(all_my_pets) > 0

    pets_info = []
    for i in range(len(all_my_pets)):
        pet_info = all_my_pets[i].text

        # избавляемся от лишних символов '\n×'
        pet_info = pet_info.split("\n")[0]

        # добавляем в список pets_info информацию рода: имя, тип, возраст,  по каждому питомцу
        pets_info.append(pet_info)


def test_show_my_pets(driver):
    driver.find_element(By.ID, 'email').send_keys('stanislav-irk@bk.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('Taisia-28.11')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # неявное ожидание
    driver.implicitly_wait(10)
    # явное ожидание
    WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                    ((By.XPATH, "//a[contains(text(),'Мои питомцы')]")))
    # либо
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located
                                    ((By.XPATH, "//button[contains(text(),'Выйти')]")))

    images = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                             ((By.CSS_SELECTOR, '.card-deck .card-img-top')))
    names = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located
                                            ((By.CSS_SELECTOR, '.card-deck .card-title')))
    descriptions = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                                   ((By.CSS_SELECTOR, '.card-deck .card-text')))

    for i in range(0):

        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
