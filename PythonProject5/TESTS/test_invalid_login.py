import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PAGES.login_page import LoginPage

@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()

    # Invalid credentials
    login_page.login("invalidemail@guvi.in", "wrongpassword")

    assert login_page.is_login_successful() == False, "Login should have failed with invalid credentials!"


