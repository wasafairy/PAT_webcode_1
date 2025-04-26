from PAGES.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()

    # Replace with valid credentials
    login_page.login("sskp22022@gmail.com", "Kani@2006")

    #Step 1 & 2: Verify login successful
    assert login_page.is_login_successful(), "Login failed!"

    #Step 3: Logout and verify
    login_page.logout()
    assert login_page.is_logged_out(), "Logout failed or user still logged in!"
