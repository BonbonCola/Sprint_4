import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest

@pytest.fixture
def browser():
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # запустили драйвер
    yield d
    time.sleep(5)
    d.quit()