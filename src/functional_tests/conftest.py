import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Pre-warm the cache at session scope
@pytest.fixture(scope="session", autouse=True)
def setup_firefox_driver():
    GeckoDriverManager().install()

# Create a new browser per test
@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
