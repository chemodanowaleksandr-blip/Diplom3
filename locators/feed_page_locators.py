from selenium.webdriver.common.by import By

class FeedPageLocators:
    ALL_TIME_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за всё время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    IN_PROGRESS_ORDERS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]")
    # Дополнительный локатор для получения номера последнего созданного заказа на странице истории/ленты
    LAST_ORDER_NUMBER = (By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'OrderHistory_number')]")
