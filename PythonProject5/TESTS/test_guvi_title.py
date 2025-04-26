from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_guvi_title():
    # Expected title
    expected_title = "GUVI | Learn to code in your native language"

    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open GUVI website
        driver.get("https://www.guvi.in")

        # Get the title of the webpage
        actual_title = driver.title
        print("Page Title:", actual_title)

        # Assert the title
        assert actual_title == expected_title, f"Title mismatch. Expected: '{expected_title}', Got: '{actual_title}'"
        print("Test Passed: Webpage title is correct.")

    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_guvi_title()
