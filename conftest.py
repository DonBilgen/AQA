import os
import time

import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver():

    path = os.path.dirname(r"C:\Users\Bil\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.7.0_0\manifest.json")
    options = Options()
    options.add_argument(f"--load-extension={path}")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    time.sleep(6)
    # Получение списка открытых вкладок
    handles = driver.window_handles
    # Переключение на  начальную вкладку
    driver.switch_to.window(handles[0])

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    yield driver

    driver.quit()