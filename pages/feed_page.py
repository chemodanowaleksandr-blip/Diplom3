import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

class FeedPage(BasePage):
    @allure.step("Получить количество заказов за всё время")
    def get_all_time_orders_count(self):
        return self.get_text_from_element(FeedPageLocators.ALL_TIME_ORDERS_COUNTER)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_in_progress_orders_text(self):
        return self.get_text_from_element(FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
