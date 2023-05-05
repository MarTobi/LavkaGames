import time
from selenium.webdriver import Keys, ActionChains
from base.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # ЛОКАТОРЫ

    payment_method = '//label[contains(text(), "Способ оплаты")]' \
                     '/ancestor::div[1]//div[@class="jq-selectbox__select-text"]'
    method_dolyami = '//li[contains(text(), "Долями")]'
    selection_pvz = '//a[contains(text(), "Выбрать ПВЗ")]'
    field_find_address = '//input[@placeholder="Поиск города"]'
    burger_cdek = '//div[@class="CDEK-widget__sidebar-burger CDEK-widget__sidebar-button"]'
    button_confirm_pvz = '//button[@data-label="Выбрать"]'
    price_delivery = '//p[@id="delivery"]'
    total_order_amount = '//p[@id="total"]'
    field_phone = '//div[@class="req"]/input[@name="phone"]'
    field_street = '//input[@name="address_street"]'
    field_house = '//input[@name="address_house"]'
    field_flat = '//input[@name="address_flat"]'
    field_zipcode = '//input[@name="zipcode"]'
    scroll_page = '//label[contains(text(),"Примечание")]'

    # ПОЛУЧЕНИЕ ЛОКАТОРОВ С УЧЕТОМ ОЖИДАНИЯ

    def get_payment_method(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.payment_method)))

    def get_method_dolyami(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.method_dolyami)))

    def get_selection_pvz(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.selection_pvz)))

    def get_field_find_address(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_find_address)))

    def get_burger_cdek(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.burger_cdek)))

    def get_address_pvz(self, address_pvz):
        address = f'// p[contains(text(), "{address_pvz}")]'
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, address)))

    def get_button_confirm_pvz(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_confirm_pvz)))

    def get_field_phone(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_phone)))

    def get_field_street(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_street)))

    def get_field_house(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_house)))

    def get_field_flat(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_flat)))

    def get_field_zipcode(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_zipcode)))

    def get_scroll_page(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.scroll_page)))

    def get_price_delivery(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_delivery)))

    def get_total_order_amount(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.total_order_amount)))

    #  ДЕЙСТВИЯ СОВРЕШАЕМЫЕ С ЭЛЕМЕНТАМИ НА СТРАНИЦЕ

    def click_payment_method(self):
        self.get_payment_method().click()
        print('Пользователь выбирает способ оплаты')

    def click_method_dolyami(self):
        self.get_method_dolyami().click()
        print('Пользователь выбирает способ оплаты - долями')

    def click_selection_pvz(self):
        self.get_selection_pvz().click()
        print('Пользователь нажал на кнпоку "выбрать ПВЗ"')

    def input_field_find_address(self, address):
        self.get_field_find_address().clear()
        self.get_field_find_address().send_keys(address)
        self.get_field_find_address().send_keys(Keys.RETURN)
        print(f'Пользователь указал город "{address}" в поле')

    def click_burger_cdek(self):
        self.get_burger_cdek().click()
        print('Пользователь нажал на бургер в поп-апе с картой')

    def select_address_pvz(self, address_pvz):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_address_pvz(address_pvz)).perform()
        self.get_address_pvz(address_pvz).click()
        print(f'Пользователь выбрал ПВЗ c названием: "{address_pvz}"')

    def click_button_confirm_pvz(self):
        self.get_button_confirm_pvz().click()
        print('Пользователь нажал "выбрать" для подтверждения адреса ПВЗ')

    def input_field_phone(self, phone):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_scroll_page()).perform()
        self.get_field_phone().send_keys(phone)
        print(f'Пользователь указал номер телефона: "+7{phone}"')

    def input_field_street(self, street):
        self.get_field_street().send_keys(street)
        print(f'Пользователь указал улицу: "{street}"')

    def input_field_house(self, house):
        self.get_field_house().send_keys(house)
        print(f'Пользователь указал дом: "{house}"')

    def input_field_flat(self, flat):
        self.get_field_flat().send_keys(flat)
        print(f'Пользователь указал квартиру: "{flat}"')

    def input_field_zipcode(self, zipcode):
        self.get_field_zipcode().send_keys(zipcode)
        print(f'Пользователь указал почтовый индекс: "{zipcode}"')

    def save_value_price_delivery(self):
        time.sleep(2)
        value_price_delivery = self.get_price_delivery().text
        return value_price_delivery

    def save_value_total_order_amount(self):
        value_total_order_amount = self.get_total_order_amount().text
        return value_total_order_amount

    # МЕТОДЫ ВОСПРОИЗВОДЯЩИЕ РАЗЛИЧНЫЕ ДЕЙСТВИЯ НА СТРАНИЦЕ

    # Выбор ПВЗ СДЭКОМ
    def select_address_cdek(self):
        self.click_selection_pvz()
        self.input_field_find_address('Омск')
        self.click_burger_cdek()
        self.select_address_pvz('На Гагарина')
        self.click_button_confirm_pvz()

    def input_contact_form(self):
        self.input_field_phone(9999999999)
        self.input_field_street("Красный путь")
        self.input_field_house("64")
        self.input_field_flat("27")
        self.input_field_zipcode("644024")
