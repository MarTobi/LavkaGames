import time


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page




# Фикстура, в которой я вынес драйвер, а также добавил авторизацию.
# В конце теста система удаляет все добавленные в корзину товары, и закрывает браузер

@pytest.fixture()
def set_up_for_buy_products():
    print("\nЗапуск теста")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/semyonplotnikov/PycharmProjects/resources/chromedriver')
    driver_g = webdriver.Chrome(options=options, service=g)
    base_url = 'https://www.lavkaigr.ru/'
    driver_g.get(base_url)
    driver_g.maximize_window()
    cp = Cart_page(driver_g)
    cp.authorization()
    cp.click_logo_to_main_page()
    yield driver_g
    print("\nТест завершен! Удаляем товар(ы) из корзины")
    cp.click_cart_icon()
    cp.click_button_checkout()
    cp.click_button_clear_cart()
    time.sleep(2)
    driver_g.quit()


