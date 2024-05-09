import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time


# Predefined configuration

URL_LOGIN_PAGE = "https://spa4h429l.otpyrc.dev/signin"

USERNAME = "sengloong82@gmail.com"

PASSWORD = "CDCQATest123"

WRONG_USERNAME = "testing123@testing123.test"

WRONG_PASSWORD = "wrongpassword"


# Predefined XPATHs for elements for the login page

XPATH_LOGIN_PAGE_HEADER_SIGN_IN_ELEMENT = "//h2[contains(text(), 'Sign In')]"

XPATH_LOGIN_PAGE_SIGN_IN_FORM_ELEMENT = "//form[contains(@method, 'POST') and contains(@action, '/oauth2/default/v1/authorize')]"

XPATH_LOGIN_PAGE_LABEL_USERNAME_ELEMENT = "//label[contains(text(), 'Username')]"

XPATH_LOGIN_PAGE_INPUT_USERNAME_ELEMENT = "//input[contains(@type, 'text') and contains(@name, 'identifier') and contains(@autocomplete, 'username')]"

XPATH_LOGIN_PAGE_LABEL_PASSWORD_ELEMENT = "//label[contains(text(), 'Password')]"

XPATH_LOGIN_PAGE_INPUT_PASSWORD_ELEMENT = "//input[contains(@type, 'password') and contains(@name, 'credentials.passcode') and contains(@autocomplete, 'current-password') and contains(@class, 'password-with-toggle')]"

XPATH_LOGIN_PAGE_LABEL_KEEP_ME_SIGNED_IN_ELEMENT = "//label[contains(text(), 'Keep me signed in')]"

XPATH_LOGIN_PAGE_CHECKBOX_KEEP_ME_SIGNED_IN_ELEMENT = "//input[contains(@type, 'checkbox') and contains(@name, 'rememberMe')]"

XPATH_LOGIN_PAGE_BUTTON_SIGN_IN_ELEMENT = "//input[contains(@type, 'submit') and contains(@value, 'Sign in') and contains(@data-type, 'save')]"

XPATH_LOGIN_PAGE_LINK_FORGOT_PASSWORD_ELEMENT = "//a[contains(text(), 'Forgot password?')]"

XPATH_LOGIN_PAGE_LINK_SIGN_UP_ELEMENT = "//a[contains(text(), 'Sign up')]"

XPATH_LOGIN_PAGE_P_ALERT_FORM_ERROR_ELEMENT = "//p[contains(text(), 'We found some errors. Please review the form and make corrections.')]"

XPATH_LOGIN_PAGE_P_ALERT_EMPTY_ELEMENT = "//p[contains(text(), 'This field cannot be left blank')]"

XPATH_LOGIN_PAGE_P_ALER_WRONG_USERNAME_OR_PASSWORD_ELEMENT = "//p[contains(text(), 'Unable to sign in')]"


# Predefined XPATHs for elements for the OTP verification page

XPATH_OTP_PAGE_HEADER_VERIFY_ELEMENT = "//h2[contains(text(), 'Verify with Google Authenticator')]"

XPATH_OTP_PAGE_LABEL_ENTER_CODE_ELEMENT = "//label[contains(text(), 'Enter code')]"

XPATH_OTP_PAGE_BUTTON_VERIFY_ELEMENT = "//input[contains(@type, 'submit') and contains(@value, 'Verify') and contains(@data-type, 'save')]"

XPATH_OTP_PAGE_SPAN_USERNAME_ELEMENT = "//span[contains(text(), '" + USERNAME + "')]"


# Predefined XPATHs for elements for the forgot password page

XPATH_FORGOT_PASSWORD_HEADER_ELEMENT = "//h2[contains(text(), 'Reset your password')]"

XPATH_FORGOT_PASSWORD_LABEL_EMAIL_USERNAME_ELEMENT = "//label[contains(text(), 'Email or Username')]"

XPATH_FORGOT_PASSWORD_BUTTON_NEXT_ELEMENT = "//input[contains(@type, 'submit') and contains(@value, 'Next') and contains(@data-type, 'save')]"


# Predefined XPATHs for elements for the sign up page

XPATH_SIGN_UP_HEADER_ELEMENT = "//h2[contains(text(), 'Sign up')]"

XPATH_SIGN_UP_LABEL_FIRST_NAME_ELEMENT = "//label[contains(text(), 'First name')]"

XPATH_SIGN_UP_INPUT_FIRST_NAME_ELEMENT = "//input[contains(@type, 'text') and contains(@name, 'userProfile.firstName')]"

XPATH_SIGN_UP_LABEL_LAST_NAME_ELEMENT = "//label[contains(text(), 'Last name')]"

XPATH_SIGN_UP_INPUT_LAST_NAME_ELEMENT = "//input[contains(@type, 'text') and contains(@name, 'userProfile.lastName')]"

XPATH_SIGN_UP_LABEL_EMAIL_ELEMENT = "//label[contains(text(), 'Email')]"

XPATH_SIGN_UP_INPUT_EMAIL_ELEMENT = "//input[contains(@type, 'text') and contains(@name, 'userProfile.email')]"

XPATH_SIGN_UP_BUTTON_SIGN_UP_ELEMENT = "//input[contains(@type, 'submit') and contains(@value, 'Sign Up') and contains(@data-type, 'save')]"


# Predefined function that contain selenium web driver configuration 

@pytest.fixture
def driver(selenium):
    
    selenium.get(URL_LOGIN_PAGE)
    
    time.sleep(2)
    
    yield selenium


# Predefined functions for checking elements for the login page


# Check the URL of the login page
def login_page_check_url(web_driver):
    
    assert 'okta.com' in web_driver.current_url


# Check for sign in form element at the login page
def login_page_check_sign_in_form_element(web_driver):

    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_SIGN_IN_FORM_ELEMENT)


# Check for sign in header element at the login page
def login_page_check_header_sign_in_element(web_driver):

    assert 'Sign In' in web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_HEADER_SIGN_IN_ELEMENT).text


# Check for username label element at the login page
def login_page_check_label_username_element(web_driver):
    
    assert 'Username' in web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_LABEL_USERNAME_ELEMENT).text
    

# Check for username input element at the login page
def login_page_check_input_username_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_INPUT_USERNAME_ELEMENT) 


# Check for password label element at the login page
def login_page_check_label_password_element(web_driver):
        
    assert 'Password' in web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_LABEL_PASSWORD_ELEMENT).text


# Check for password input element at the login page
def login_page_check_input_password_element(web_driver):
        
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_INPUT_PASSWORD_ELEMENT)


# Check for keep me signed in label element at the login page
def login_page_check_label_keep_me_signed_in_element(web_driver):
            
    assert 'Keep me signed in' in web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_LABEL_KEEP_ME_SIGNED_IN_ELEMENT).text


# Check for keep me signed in checkbox element at the login page
def login_page_check_checkbox_keep_me_signed_in_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_CHECKBOX_KEEP_ME_SIGNED_IN_ELEMENT)


# Check for sign in button element at the login page
def login_page_check_button_sign_in_element(web_driver):
        
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_BUTTON_SIGN_IN_ELEMENT)


# Check for forgot password link element at the login page
def login_page_check_link_forgot_password_element(web_driver):
    
    assert 'Forgot password?' in web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_LINK_FORGOT_PASSWORD_ELEMENT).text


# Check for sign up link element at the login page
def login_page_check_link_sign_up_element(web_driver):
    
    assert 'Sign up' in web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_LINK_SIGN_UP_ELEMENT).text


# Predefined function for filling up the login form and click at sign in
def login_page_filling_up_login_form_and_sign_in(web_driver, login_username, login_password):
    
    ac = ActionChains(web_driver)
    
    username_input = web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_INPUT_USERNAME_ELEMENT)
    
    ac.move_to_element(username_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(username_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(username_input).click().send_keys(login_username).perform()
    
    time.sleep(1)
    
    password_input = web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_INPUT_PASSWORD_ELEMENT)
    
    ac.move_to_element(password_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(password_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(password_input).click().send_keys(login_password).perform()
    
    time.sleep(1)
    
    signin_button = web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_BUTTON_SIGN_IN_ELEMENT)
    
    ac.move_to_element(signin_button).perform()
    
    time.sleep(1)
    
    ac.move_to_element(signin_button).click().perform()
    
    time.sleep(2)
    
    return web_driver


# Unit tests for the login page


def test_url_index_page(driver):
    
    login_page_check_url(driver)


def test_login_page_check_sign_in_form_element(driver):
    
    login_page_check_sign_in_form_element(driver)


def test_login_page_check_header_sign_in_element(driver):
    
    login_page_check_header_sign_in_element(driver)


def test_login_page_check_label_username_element(driver):
    
    login_page_check_label_username_element(driver)


def test_login_page_check_input_username_element(driver):
    
    login_page_check_input_username_element(driver)


def test_login_page_check_label_password_element(driver):
    
    login_page_check_label_password_element(driver)


def test_login_page_check_input_password_element(driver):
    
    login_page_check_input_password_element(driver)


def test_login_page_check_label_keep_me_signed_in_element(driver):
    
    login_page_check_label_keep_me_signed_in_element(driver)


def test_login_page_check_checkbox_keep_me_signed_in_element(driver):
    
    login_page_check_checkbox_keep_me_signed_in_element(driver)


def test_login_page_check_button_sign_in_element(driver):
    
    login_page_check_button_sign_in_element(driver)


def test_login_page_check_link_forgot_password_element(driver):
    
    login_page_check_link_forgot_password_element(driver)
    

def test_login_page_check_link_sign_up_element(driver):
    
    login_page_check_link_sign_up_element(driver)
    

# Test cases based on scenarios

# Validate the login page
def test_validate_login_page_suite(driver):
    
    print("start testing test_validate_login_page_suite\n")
    
    login_page_check_url(driver)
    
    login_page_check_sign_in_form_element(driver)
    
    login_page_check_header_sign_in_element(driver)
    
    login_page_check_label_username_element(driver)
    
    login_page_check_input_username_element(driver)
    
    login_page_check_label_password_element(driver)
    
    login_page_check_input_password_element(driver)
    
    login_page_check_label_keep_me_signed_in_element(driver)
    
    login_page_check_checkbox_keep_me_signed_in_element(driver)
    
    login_page_check_button_sign_in_element(driver)
    
    login_page_check_link_forgot_password_element(driver)
    
    login_page_check_link_sign_up_element(driver)
    
    print("\nend testing test_validate_login_page_suite")
    

# Test case on submitting the login form without username and password
@pytest.mark.parametrize("name, password", [pytest.param("", "")])
def test_login_page_sign_in_without_username_and_password(driver, name, password):
    
    print("start testing test_login_page_sign_in_without_username_and_password\n")
    
    web_driver = login_page_filling_up_login_form_and_sign_in(driver, name, password)
    
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_P_ALERT_FORM_ERROR_ELEMENT)
    
    assert len(web_driver.find_elements(By.XPATH, XPATH_LOGIN_PAGE_P_ALERT_EMPTY_ELEMENT)) == 2
    
    print("\nend testing test_login_page_sign_in_without_username_and_password")
    

# Test case on submitting the login form with username but without password
@pytest.mark.parametrize("name, password", [pytest.param(USERNAME, "")])
def test_login_page_sign_in_using_username_without_password(driver, name, password):
    
    print("start testing test_login_page_sign_in_using_username_without_password\n")
    
    web_driver = login_page_filling_up_login_form_and_sign_in(driver, name, password)
    
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_P_ALERT_FORM_ERROR_ELEMENT)
    
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_P_ALERT_EMPTY_ELEMENT)
    
    print("\nend testing test_login_page_sign_in_using_username_without_password")


# Test case on submitting the login form without username but with password
@pytest.mark.parametrize("name, password", [pytest.param("", PASSWORD)])
def test_login_page_sign_in_using_password_without_username(driver, name, password):
    
    print("start testing test_login_page_sign_in_using_password_without_username\n")
    
    web_driver = login_page_filling_up_login_form_and_sign_in(driver, name, password)
    
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_P_ALERT_FORM_ERROR_ELEMENT)
    
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_P_ALERT_EMPTY_ELEMENT)
    
    print("\nend testing test_login_page_sign_in_using_password_without_username")
    

# Test case on submitting the login form with wrong username and password
@pytest.mark.parametrize("name, password", [pytest.param(WRONG_USERNAME, WRONG_PASSWORD)])
def test_login_page_sign_in_using_wrong_username_and_password(driver, name, password):
    
    print("start testing test_login_page_sign_in_using_wrong_username_and_password\n")
    
    web_driver = login_page_filling_up_login_form_and_sign_in(driver, name, password)
    
    assert 'Unable to sign in' in web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_P_ALER_WRONG_USERNAME_OR_PASSWORD_ELEMENT).text
    
    print("\nend testing test_login_page_sign_in_using_wrong_username_and_password")


# Test case on submitting the login form with correct username and password
@pytest.mark.parametrize("name, password", [pytest.param(USERNAME, PASSWORD)])
def test_login_page_sign_in_using_correct_username_and_password(driver, name, password):
    
    print("start testing test_login_page_sign_in_using_correct_username_and_password\n")
    
    web_driver = login_page_filling_up_login_form_and_sign_in(driver, name, password)
    
    assert '/oauth2/default/v1/authorize' in web_driver.current_url
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_HEADER_VERIFY_ELEMENT)
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_LABEL_ENTER_CODE_ELEMENT)
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_BUTTON_VERIFY_ELEMENT)
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_SPAN_USERNAME_ELEMENT)
    
    print("\nend testing test_login_page_sign_in_using_correct_username_and_password")
    

# Test case on clicking the forgot password link at the login page
def test_login_page_click_forgot_password_link(driver):
    
    print("start testing test_login_page_click_forgot_password_link\n")
    
    ac = ActionChains(driver)
    
    forgot_password_link = driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_LINK_FORGOT_PASSWORD_ELEMENT)
    
    ac.move_to_element(forgot_password_link).perform()
    
    time.sleep(1)
    
    ac.move_to_element(forgot_password_link).click().perform()
    
    time.sleep(2)
    
    assert "Reset your password" in driver.find_element(By.XPATH, XPATH_FORGOT_PASSWORD_HEADER_ELEMENT).text
    
    assert driver.find_element(By.XPATH, XPATH_FORGOT_PASSWORD_LABEL_EMAIL_USERNAME_ELEMENT)
    
    assert driver.find_element(By.XPATH, XPATH_FORGOT_PASSWORD_BUTTON_NEXT_ELEMENT)
    
    print("\nend testing test_login_page_click_forgot_password_link")
    

# Test case on clicking the sign up link at the login page
def test_login_page_click_sign_up_link(driver):
    
    print("start testing test_login_page_click_sign_up_link\n")
    
    ac = ActionChains(driver)
    
    sign_up_link = driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_LINK_SIGN_UP_ELEMENT)
    
    ac.move_to_element(sign_up_link).perform()
    
    time.sleep(1)
    
    ac.move_to_element(sign_up_link).click().perform()
    
    time.sleep(2)
    
    assert 'Sign up' in driver.find_element(By.XPATH, XPATH_SIGN_UP_HEADER_ELEMENT).text
    
    assert driver.find_element(By.XPATH, XPATH_SIGN_UP_LABEL_FIRST_NAME_ELEMENT)
    
    assert driver.find_element(By.XPATH, XPATH_SIGN_UP_INPUT_FIRST_NAME_ELEMENT)
    
    assert driver.find_element(By.XPATH, XPATH_SIGN_UP_LABEL_LAST_NAME_ELEMENT)
    
    assert driver.find_element(By.XPATH, XPATH_SIGN_UP_INPUT_LAST_NAME_ELEMENT)
    
    assert driver.find_element(By.XPATH, XPATH_SIGN_UP_LABEL_EMAIL_ELEMENT)
    
    assert driver.find_element(By.XPATH, XPATH_SIGN_UP_INPUT_EMAIL_ELEMENT)
    
    assert driver.find_element(By.XPATH, XPATH_SIGN_UP_BUTTON_SIGN_UP_ELEMENT)
    
    print("\nend testing test_login_page_click_sign_up_link")