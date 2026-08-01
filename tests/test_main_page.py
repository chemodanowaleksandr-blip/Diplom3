import pytest
import allure
import data
from pages.main_page import MainPage
from pages.feed_page import FeedPage

@allure.epic("Stellar Burgers UI")
@allure.feature("Главная страница")
class TestMainPage:

    @allure.story("Успешный переход по клику на 'Ленту заказов'")
    def test_navigation_to_order_feed_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_order_feed_button()
        
        # Проверяем, что URL изменился на адрес ленты
        assert driver.current_url == data.FEED_URL, "Не удалось перейти в Ленту заказов"

    @allure.story("Успешный переход обратно в 'Конструктор' с другой страницы")
    def test_navigation_to_constructor_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Открываем Ленту через метод страницы, БЕЗ прямого driver.get()
        feed_page.open_feed_page()
        
        main_page.click_constructor_button()
        
        # Проверяем, что URL вернулся на главную
        assert driver.current_url == data.BASE_URL, "Не удалось вернуться в Конструктор"

    @allure.story("Открытие модального окна с деталями ингредиента")
    def test_click_ingredient_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_first_ingredient()
        
        assert main_page.is_modal_details_visible(), "Модальное окно с деталями не открылось"

    @allure.story("Закрыть модальное окно ингредиента кликом на крестик")
    def test_close_modal_by_click_on_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_first_ingredient()
        main_page.click_close_modal_button()
        
        # Небольшая пауза для анимации скрытия из DOM
        driver.implicitly_wait(1)
        assert not main_page.is_modal_details_visible(), "Модальное окно не закрылось"
