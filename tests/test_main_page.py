import pytest
import allure
from pages.main_page import MainPage

@allure.feature("Главная страница Stellar Burgers")
class TestMainPage:

    @allure.story("Проверка переходов по клику на разделы")
    def test_navigation_to_constructor_and_feed(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            driver.get("https://nomoreparties.site")
            
        with allure.step("Кликнуть на Ленту Заказов"):
            main_page.click_order_feed_button()
            assert "feed" in driver.current_url, "Не удалось перейти в Ленту заказов"
            
        with allure.step("Кликнуть на Конструктор"):
            main_page.click_constructor_button()
            assert driver.current_url == "https://nomoreparties.site", "Не удалось вернуться в Конструктор"

    @allure.story("Модальное окно ингредиентов")
    def test_click_ingredient_opens_modal_and_closes(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            driver.get("https://nomoreparties.site")
            
        with allure.step("Кликнуть на первый ингредиент"):
            main_page.click_first_ingredient()
            assert main_page.is_modal_details_visible(), "Модальное окно с деталями не открылось"
            
        with allure.step("Закрыть модальное окно кликом на крестик"):
            main_page.click_close_modal_button()
            # Добавим небольшое неявное ожидание, чтобы окно успело скрыться из DOM, если нужно
            driver.implicitly_wait(1)
