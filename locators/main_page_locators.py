from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    INGREDIENT_CARD = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    MODAL_DETAILS = (By.XPATH, ".//div[contains(@class, 'Modal_modal_opened')]")
    BASKET_AREA = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')]")
