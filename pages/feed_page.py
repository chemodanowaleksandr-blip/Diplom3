import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
import data

class FeedPage(BasePage):

    @allure.step("Открыть страницу Ленты заказов")
    def open_feed_page(self):
        # Используем метод базового класса БЕЗ прямого обращения к драйверу
        self.open_url(data.FEED_URL)

    @allure.step("Получить текущее значение счётчика 'Выполнено за всё время'")
    def get_all_time_orders_count(self):
        return self.get_text_from_element(FeedPageLocators.ALL_TIME_ORDERS_COUNTER)

    @allure.step("Получить текущее значение счётчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Получить текст заказа из блока 'В работе'")
    def get_in_progress_orders_text(self):
        return self.get_text_from_element(FeedPageLocators.IN_PROGRESS_ORDERS_BLOCK)
