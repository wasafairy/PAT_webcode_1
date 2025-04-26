from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Or use Edge/Firefox depending on your setup
    driver.maximize_window()
    yield driver
    driver.quit()

def test_sign_up_redirect(driver):
    # 1. Open Guvi homepage
    driver.get("https://www.guvi.in/")

    # 2. Click on the "Sign Up" button
    sign_up_button = driver.find_element(By.LINK_TEXT, "Sign up")
    sign_up_button.click()

    # 3. Verify if the page redirected correctly
    expected_url = "https://www.guvi.in/sign-in/"
    assert driver.current_url == expected_url, f"Redirection failed! Current URL is {driver.current_url}"

    print("Sign Up button redirects correctly!")
