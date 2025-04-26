import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    yield driver
    driver.quit()

def test_signup_button_visibility(driver):
    signup_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sign up"))
    )
    assert signup_button.is_displayed(), "Sign-up button is not visible."

def test_signup_button_clickable(driver):
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign up"))
    )
    assert signup_button.is_enabled(), "Sign-up button is not clickable."
