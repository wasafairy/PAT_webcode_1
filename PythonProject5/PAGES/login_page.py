from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.guvi.in/sign-in/"
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")
        self.profile_icon = (By.CSS_SELECTOR, "img[alt='profile']")
        self.sign_out = (By.XPATH, "//div[@id='dropdown_contents' and text()='Sign Out']")

    def load(self):
        self.driver.get(self.url)

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_field)).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.profile_icon)
            )
            return True
        except:
            return False

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.profile_icon)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_out)
        ).click()

    def is_logged_out(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.login_button)
            )
            return True
        except:
            return False

