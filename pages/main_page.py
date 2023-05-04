from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from base.base_page import Base


class Main_page(Base):
    # def __init__(self, driver_g):
    #     super().__init__(driver_g)
    #     self.driver_g = driver_g

    # ЛОКАТОРЫ

    # Локаторы для фильтров
    min_price = '//input[@name="price__gte"]'
    max_price = '//input[@name="price__lte"]'
    checkbox_in_stock = '//label[@for="stocks"]'
    checkbox_lavka_igr = '//label[@for="factory-11"]'
    checkbox_gaga_games = '//label[@for="factory-43"]'
    checkbox_hobby_world = '//label[@for="factory-1"]'
    checkbox_crowd_games = '//label[@for="factory-125"]'
    checkbox_russian = '//label[@for="lang-6"]'
    slider_publisher = '//h2[contains(text(), "Издатель")]/..//div[@class="jspDrag"]'
    slider_language = '//h2[contains(text(), "Язык")]/..//div[@class="jspDrag"]'
    title_time_game = '//div[@class="section tobo check-list"]/..//h2[contains(text(), "Время партии")]'
    button_submit_filter = '//a[@id="submit_filter"]'
    button_pagenator = '//li[@class="next"]'

    # ПОЛУЧЕНИЕ ЛОКАТОРОВ С УЧЕТОМ ОЖИДАНИЯ

    # Для получения фильтров

    def get_min_price(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_checkbox_in_stock(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_in_stock)))

    def get_title_time_game(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title_time_game)))

    def get_checkbox_lavka_igr(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_lavka_igr)))

    def get_checkbox_gaga_games(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_gaga_games)))

    def get_checkbox_hobby_world(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_hobby_world)))

    def get_checkbox_russian(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_russian)))

    def get_checkbox_crowd_games(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_crowd_games)))

    def get_slider_publisher(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.slider_publisher)))

    def get_slider_language(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.slider_language)))

    def get_button_submit_filter(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_submit_filter)))

    # Для товаров

    def get_name_product(self, name_product):
        locator_name_product = f'//a[@class="game-name" and contains(text(), "{name_product}")]'
        return WebDriverWait(self.driver_g, 5).until(
            EC.element_to_be_clickable((By.XPATH, locator_name_product)))

    def get_price_product(self, name_product):
        price_product = f'//a[@class="game-name" and contains(text(), "{name_product}")]' \
                        f'/ancestor::div[1]//p[@class="price"]'
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, price_product)))

    def get_button_more(self, name_product):
        locator_button_more = f'//a[@class="game-name" and contains(text(), "{name_product}")]'
        f'/ancestor::div[1]//a[contains(text(), "подробнее")]'
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, locator_button_more)))

    def get_button_buy(self, name_product):
        locator_button_buy = f'//a[@class="game-name" and contains(text(), "{name_product}")]' \
                             f'/ancestor::div[1]//a[@class="btn buy-mini" and contains(text(), "Купить")]'
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, locator_button_buy)))

    # Для навигации

    def get_button_pagenator(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_pagenator)))

    #  ДЕЙСТВИЯ, СОВЕРШАЕМЫЕ С ЭЛЕМЕНТАМИ НА СТРАНИЦЕ

    # Действия с фильтрами

    def input_min_price(self, price):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_min_price()).perform()
        self.get_min_price().clear()
        self.get_min_price().send_keys(price)
        print(f'Пользователь задал минимальную цену товара: "{price} р"')

    def input_max_price(self, price):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_max_price()).perform()
        self.get_max_price().clear()
        self.get_max_price().send_keys(price)
        print(f'Пользователь задал максимальную цену товара: "{price} р"')

    def click_checkbox_in_stock(self):
        actions = ActionChains(self.driver_g)
        actions.click_and_hold(self.get_checkbox_in_stock()).perform()
        self.get_checkbox_in_stock().click()
        print('Пользователь отсортировал игры по наличию')

    def scroll_to_title__time_game(self):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_title_time_game()).perform()

    def click_checkbox_crowd_games(self):
        actions = ActionChains(self.driver_g)
        actions.click_and_hold(self.get_slider_publisher()).move_by_offset(0, 86).release().perform()
        self.get_checkbox_crowd_games().click()
        print('Пользователь отсортировал игры по издательству "Crowd Games"')

    def click_checkbox_lavka_igr(self):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_checkbox_lavka_igr()).perform()
        self.get_checkbox_lavka_igr().click()
        print('Пользователь отсортировал игры по издательству "Лавка Игр"')

    def click_checkbox_gaga_games(self):
        actions = ActionChains(self.driver_g)
        actions.click_and_hold(self.get_slider_publisher()).move_by_offset(0, 80).release().perform()
        self.get_checkbox_gaga_games().click()
        print('Пользователь отсортировал игры по издательству "GaGa Games"')

    def click_checkbox_hobby_world(self):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_checkbox_hobby_world()).perform()
        self.get_checkbox_hobby_world().click()
        print('Пользователь отсортировал игры по издательству "Hobby World"')

    def click_checkbox_russian(self):
        actions = ActionChains(self.driver_g)
        actions.click_and_hold(self.get_slider_language()).move_by_offset(0, 107).release().perform()
        self.get_checkbox_russian().click()
        print('Пользователь отсортировал игры по языку')

    def click_button_submit_filter(self):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_button_submit_filter()).perform()
        self.get_button_submit_filter().click()
        print('Пользователь нажал кнопку "применить фильтр"')

    # Действия с продуктами

    def click_button_more(self, name_product):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_button_more(name_product)).perform()
        self.get_button_more(name_product).click()
        print(f'Пользователь перешел на страницу настольной игры: "{name_product}"')

    def click_button_buy(self, name_product):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_button_buy(name_product)).perform()
        self.get_value_price_product(name_product)
        self.get_button_buy(name_product).click()
        print(f'Пользователь нажал на кнопку "купить" у настольной игры: "{name_product}".')

    def get_value_price_product(self, name_product):
        price_product = self.get_price_product(name_product).text
        print(f'Цена настольной игры "{name_product}": "{price_product}"')

    # Действия с навигацией

    def click_button_pagenator(self):
        actions = ActionChains(self.driver_g)
        actions.move_to_element(self.get_button_pagenator()).perform()
        self.get_button_pagenator().click()

    # МЕТОДЫ ВОСПРОИЗВОДЯЩИЕ РАЗЛИЧНЫЕ ДЕЙСТВИЯ НА САЙТЕ

    # Работа с фильтрами

    def select_filters(self):
        self.input_min_price(200)
        self.input_max_price(15000)
        self.click_checkbox_in_stock()
        self.scroll_to_title__time_game()
        self.click_checkbox_lavka_igr()
        self.click_checkbox_hobby_world()
        self.click_checkbox_crowd_games()
        self.click_checkbox_gaga_games()
        self.click_checkbox_russian()
        self.click_button_submit_filter()

    # Найти определенный продукт на сайте, если он не найден на странице, то тест переходит к следующей странице
    def find_specific_product(self, name_product):
        activate = False
        while not activate:
            try:
                if self.get_name_product(name_product).text == name_product:
                    print(f'Настольная игра {name_product} найдена')
                    self.get_value_price_product(name_product)
                    self.get_button_more(name_product)
            except TimeoutException:
                self.click_button_pagenator()
                print(f'Настольная игра {name_product} не найдена, осуществляется переход на следующую страницу')
                continue
            activate = True
        self.click_button_more(name_product)
