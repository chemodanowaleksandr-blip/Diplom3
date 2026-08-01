import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Запуск без графического экрана
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # Запуск без графического экрана
        driver = webdriver.Firefox(options=options)
    
    driver.set_window_size(1920, 1080)
    
    yield driver
    
    driver.quit()
