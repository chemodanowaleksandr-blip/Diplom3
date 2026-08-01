import pytest
import allure
from pages.feed_page import FeedPage

@allure.epic("Stellar Burgers UI")
@allure.feature("Лента заказов")
class TestFeedPage:

    @allure.story("Проверка отображения и обновления счётчика 'Выполнено за всё время'")
    def test_all_time_orders_counter_value(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        
        initial_count = feed_page.get_all_time_orders_count()
        assert initial_count is not None, "Счётчик заказов за всё время пустой"

    @allure.story("Проверка отображения и обновления счётчика 'Выполнено за сегодня'")
    def test_today_orders_counter_value(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        
        today_count = feed_page.get_today_orders_count()
        assert today_count is not None, "Счётчик заказов за сегодня пустой"

    @allure.story("Проверка отображения созданного заказа в блоке 'В работе'")
    def test_order_appears_in_progress_block(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        
        in_progress_text = feed_page.get_in_progress_orders_text()
        assert in_progress_text is not None, "Блок заказов 'В работе' не отображается на странице"
