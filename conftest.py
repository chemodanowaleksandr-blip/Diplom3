import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless") # Раскомментируй, если тесты будут падать в CI без экрана
        driver = webdriver.webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.webdriver.Firefox(options=options)
    
    driver.set_window_size(1920, 1080)
    
    yield driver
    
    driver.quit()
