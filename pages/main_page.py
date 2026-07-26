import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Кликнуть по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть по кнопке 'Лента Заказов'")
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть по первому ингредиенту")
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Проверить видимость модального окна с деталями")
    def is_modal_details_visible(self):
        return self.wait_for_visibility(MainPageLocators.MODAL_DETAILS).is_displayed()

    @allure.step("Закрыть модальное окно кликом по крестику")
    def click_close_modal_button(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)
