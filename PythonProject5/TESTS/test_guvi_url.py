from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager


def test_guvi_url():
    try:
        # Setup Chrome driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Maximize window and open the URL
        driver.maximize_window()
        driver.get("https://www.guvi.in")

        # Get the current URL and validate it
        current_url = driver.current_url
        assert "guvi.in" in current_url, f"Expected URL to contain 'guvi.in' but got {current_url}"
        print("URL is valid and working.")

    except WebDriverException as e:
        print("WebDriver Exception occurred:", e)

    finally:
        # Always close the browser
        driver.quit()


# Run the test
if __name__ == "__main__":
    test_guvi_url()
