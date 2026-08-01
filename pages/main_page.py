import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import data

class MainPage(BasePage):

    @allure.step("Открыть главную страницу Stellar Burgers")
    def open_main_page(self):
        # Используем метод базового класса, как просила Ирина
        self.open_url(data.BASE_URL)

    @allure.step("Кликнуть по кнопке 'Лента Заказов'")
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть по первому ингредиенту")
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Проверить видимость модального окна с деталями ингредиента")
    def is_modal_details_visible(self):
        return self.wait_for_visibility(MainPageLocators.MODAL_DETAILS)

    @allure.step("Закрыть модальное окно кликом на крестик")
    def click_close_modal_button(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)
