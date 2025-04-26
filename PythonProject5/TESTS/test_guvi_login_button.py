from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

def test_login_button_visibility_and_clickability():
    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the GUVI website
        driver.get("https://www.guvi.in")

        # Wait for the Login button to be present in the DOM
        wait = WebDriverWait(driver, 10)

        # Find the Login button
        login_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))

        # Test 1: Visibility
        assert login_button.is_displayed(), "Login button is not visible."
        print("Test 1 Passed: Login button is visible.")

        # Test 2: Clickability
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        print("Test 2 Passed: Login button is clickable.")

    except TimeoutException:
        print("Timeout: Login button was not found or clickable in time.")

    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_login_button_visibility_and_clickability()
