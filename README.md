# pat_webcode_1

# GUVI Web Automation Test Suite

This project is a Selenium + PyTest based automation framework created to test the GUVI sign-in and sign-up functionalities.


## Project Structure

GUVI_PROJ1/
|--.venv/ # Virtual environment 
|--PAGES/ # Page Object Model (POM) files
|---login_page.py
|--reports/
|---guvi_login_logout_report.html # HTML report (auto-generated) 
|---report.html 
|--TESTS/ # Test case implementations
|---test_guvi_login_button.py
|---test_guvi_title.py
|---test_guvi_url.py
|---test_invalid_login.py
|---test_login_logout.py
|---test_sign_up_button.py 
|---test_sign_up_redirect.py 
|--utils/
|---driver_setup.py # common driver setup logic
|--conftest.py # PyTest fixture to initialize browser 
|--requirements.txt # Required dependencies
|--README.md # Project documentation
|--.gitignore



## Test Scenarios Covered

Test-Case 1: Validate GUVI Homepage Title
- Check whether the homepage title is displayed correctly.

Test-Case 2: Verify the GUVI URL
- Validate whether the loaded URL matches the expected one.

Test-Case 3: Login Button Functionality
- Check if the Login button is:
  - Visible
  - Clickable

Test-Case 4: Sign-Up Button Functionality
- Check if the Sign-Up button is:
  - Visible
  - Clickable

Test-Case 5: Redirect to Login Page
- Click on the URL `https://www.guvi.in/sign-in/` and ensure redirection.

Test-Case 6: Valid Login & Logout
- Login with valid credentials
- Verify successful login
- Perform logout
- Validate successful logout

Test-Case 7: Invalid Login
- Login with incorrect credentials
- Catch and assert the displayed error message

---
## Running Tests
Run All Tests:

pytest --html=reports/report.html

Run Specific Test:

pytest TESTS/test_login_logout.py --html=reports/report.html

## Notes
  1. While excecuting the 5th task the given link is for the login page but the task had mentioned to ensure whther it directs to the sign up page so the task fails
## Dependencies
List of major tools/libraries used:
  1. Python 3.8+
  2. Selenium
  3. PyTest
  4. WebDriver-Manager
  5. PyTest-HTML

THIS PROJECT WAS COMPLETED BY KANISHKA S
