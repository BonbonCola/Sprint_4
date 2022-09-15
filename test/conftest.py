import time

from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

import pytest


@pytest.fixture(scope="function")
def browser():
    d = webdriver.Firefox(service=Service(GeckoDriverManager().install()))  # запустили драйвер
    yield d
    d.quit()
