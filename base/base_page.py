import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():
    def __init__(self, driver_g):
        self.driver_g = driver_g

    # Информация об урл, которая будет открываться при запуске теста

    base_url = 'https://www.lavkaigr.ru/'

    # ЛОКАТОРЫ

    # Для навигации

    logo_to_main_page = '//div[@class="logo"]'
    cart_icon = '//div[@class="cart"]//a'
    button_checkout = '//div[@class="cart open"]//a[@href="/shop/cart/"]'

    # Для авторизации

    login_button = '//a[@data-src="#autorization"]'
    email_input = '//div[@id="autorization"]//input[@name="login"]'
    password_input = '//div[@id="autorization"]//input[@name="password"]'
    authorization_button = '//a[contains(text(), "Войти")]'
    confirm_word = '//div[@class="box tobo"]/h2'

    # Для поп-апов

    pop_up_add_to_cart = '//div[@id="add-to-cart"]'
    button_go_to_cart = '//a[@class="btn" and contains(text(), "Оформить заказ")]'
    button_go_to_catalog = '//a[contains(text(), "Вернуться в каталог")]'

    # ПОЛУЧЕНИЕ ЛОКАТОРОВ С УЧЕТОМ ОЖИДАНИЯ

    # Для навигации

    def get_logo_to_main_page(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.logo_to_main_page)))

    def get_cart_icon(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_icon)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    # Для авторизации

    def get_login_button(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_email_input(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_input)))

    def get_password_input(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_input)))

    def get_authorization_button(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.authorization_button)))

    # Для поп-апов

    def get_pop_up_add_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.pop_up_add_to_cart)))

    def get_button_go_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_go_to_cart)))

    def get_button_go_to_catalog(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_go_to_catalog)))

    # Для подтверждения перехода на страницу

    def get_confirm_word(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_word)))

    # ДЕЙСТВИЯ СОВРЕШАЕМЫЕ С ЛОКАТОРАМИ (ЭЛЕМЕНТАМИ НА СТРАНИЦЕ)

    # Авторизация пользователя

    def click_login_button(self):
        self.get_login_button().click()
        print('Пользователь нажал кнопку "авторизации" в хедере')

    def enter_email_input(self):
        self.get_email_input().send_keys("gwynwildlp@rambler.ru")
        print('Пользователь ввел логин')

    def enter_password_input(self):
        self.get_password_input().send_keys("qG6pzfDzJK")
        print('Пользователь ввел пароль')

    def click_authorization_button(self):
        self.get_authorization_button().click()
        print('Пользователь нажал на кнопку "войти"')

    # Для навигации

    def click_logo_to_main_page(self):
        self.get_logo_to_main_page().click()
        print('Пользователь нажал на логотип в хедере для возврата на главную страницу')

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print('Пользователь нажал на иконку в корзине хедере')

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print('Пользователь нажал на кнопку "оформить заказ" для перехода в корзину')

    # Для проверок

    def check_go_to_page(self, check_value, confirm_value):
        actual_value = check_value.text
        assert actual_value == confirm_value
        print('Пользователь успешно перешел на следующую страницу')

    def order_amount_comparison(self, price_cart, price_delivery, price_checkout):
        price_cart = price_cart.replace("руб", "")
        price_cart = price_cart.replace(" ", "")
        price_delivery = price_delivery.replace("руб", "")
        price_delivery = price_delivery.replace(" ", "")
        price_cart = int(price_cart) + int(price_delivery)
        price_checkout = price_checkout.replace("руб", "")
        price_checkout = price_checkout.replace(" ", "")
        price_checkout = int(price_checkout)
        assert price_cart == price_checkout
        print(f'Cумма на странице корзины (с учетом доставки) и на странице чекаута равна.'
              f' Стоимость заказа: "{price_checkout} руб"')

    def make_screenshots(self):
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot {current_date}.png'
        self.driver_g.save_screenshot(f"/Users/semyonplotnikov/PycharmProjects/"
                                      f"LavkaGames_project/screen/{name_screenshot}")

    # Для поп-апов

    def click_button_go_to_cart(self):
        self.get_button_go_to_cart().click()
        print('Пользователь нажал на кнопку "оформить заказ" в поп-апе')

    def click_button_go_to_catalog(self):
        self.get_button_go_to_catalog().click()
        print('Пользователь нажал на кнопку "вернуться в каталог" в поп-апе')

    # МЕТОДЫ ВОСПРОИЗВОДЯЩИЕ РАЗЛИЧНЫЕ ДЕЙСТВИЯ НА САЙТЕ

    # Авторизация

    def authorization(self):
        self.driver_g.get(self.base_url)
        self.driver_g.maximize_window()
        self.click_login_button()
        self.enter_email_input()
        self.enter_password_input()
        self.click_authorization_button()
        self.check_go_to_page(self.get_confirm_word(), "ПЕРСОНАЛЬНЫЕ ДАННЫЕ")
