from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import Base


class Product_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # ЛОКАТОРЫ

    # Локаторы для добавления товара в корзину

    button_buy = '//div[@class="rgt-col"]//button[@class="buy-large"]'
    field_quantity = '//div[@class="rgt-col"]//input[@id="qty-large"]'

    # Для навигации

    button_back_page = '//a[@class="btn btn-white back"]'

    # ПОЛУЧЕНИЕ ЛОКАТОРОВ С УЧЕТОМ ОЖИДАНИЯ

    # Локаторы для добавления товара в корзину

    def get_button_buy(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_field_quantity(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_quantity)))

    # Для навигации

    def get_button_back_page(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_back_page)))

    #  ДЕЙСТВИЯ СОВЕРШАЕМЫЕ С ЛОКАТОРАМИ НА СТРАНИЦЕ

    def click_button_buy(self):
        self.get_button_buy().click()
        print('Пользователь нажал кнопку "купить"')

    def input_field_quantity(self, quantity):
        self.get_field_quantity().clear()
        self.get_field_quantity().send_keys(quantity)
        print(f'Пользователь указал количество товаров в размере: {quantity} шт.')
