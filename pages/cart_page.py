from selenium.webdriver import Keys

from base.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Cart_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # ЛОКАТОРЫ

    field_promocode = '//input[@name="code"]'
    confirm_promocode = '//div[contains(text(), "Промокод успешно применён")]'
    cart_price = '//p[@id="itogo"]'
    button_go_to_checkout = '//a[@id="checkout"]'
    button_clear_cart = '//a[@id="clear_cart"]'

    # ПОЛУЧЕНИЕ ЛОКАТОРОВ С УЧЕТОМ ОЖИДАНИЯ

    def get_field_promocode(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_promocode)))

    def get_confirm_promocode(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_promocode)))

    def get_cart_price(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_price)))

    def get_button_go_to_checkout(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_go_to_checkout)))

    def get_button_clear_cart(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_clear_cart)))

    #  ДЕЙСТВИЯ СОВРЕШАЕМЫЕ С ЭЛЕМЕНТАМИ НА СТРАНИЦЕ

    def input_field_promocode(self, promocode):
        self.get_field_promocode().send_keys(promocode)
        self.get_field_promocode().send_keys(Keys.RETURN)
        print(f'Пользователь ввел промокод "{promocode}" на странице корзины')

    def check_confirm_promocode(self):
        confirm_promocode = self.get_confirm_promocode().text
        assert confirm_promocode == "Промокод успешно применён"
        print("Промокод успешно активирован!")

    def save_value_cart_price(self):
        time.sleep(2)
        cart_price = self.get_cart_price().text
        return cart_price

    def click_button_go_to_checkout(self):
        self.get_button_go_to_checkout().click()
        print('Пользователь нажал кнопку "оформить заказ"')

    def click_button_clear_cart(self):
        self.get_button_clear_cart().click()
        print('Пользователь нажал кнопку "Очистить корзину"')
