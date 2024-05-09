import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

import pyotp


# Predefined configuration

URL_LOGIN_PAGE = "https://spa4h429l.otpyrc.dev/signin"

URL_MY_PROFILE_PAGE = "https://spa4h429l.otpyrc.dev/profile"

USERNAME = "sengloong82@gmail.com"

PASSWORD = "CDCQATest123"

OTP_SECRET = "25TBJTZ3JDJPSZNC"


# Predefined XPATHs for elements for the login page

XPATH_LOGIN_PAGE_INPUT_USERNAME_ELEMENT = "//input[contains(@type, 'text') and contains(@name, 'identifier') and contains(@autocomplete, 'username')]"

XPATH_LOGIN_PAGE_INPUT_PASSWORD_ELEMENT = "//input[contains(@type, 'password') and contains(@name, 'credentials.passcode') and contains(@autocomplete, 'current-password') and contains(@class, 'password-with-toggle')]"

XPATH_LOGIN_PAGE_BUTTON_SIGN_IN_ELEMENT = "//input[contains(@type, 'submit') and contains(@value, 'Sign in') and contains(@data-type, 'save')]"


# Predefined XPATHs for elements for the OTP verification page

XPATH_OTP_PAGE_INPUT_ENTER_CODE_ELEMENT = "//input[contains(@type, 'text') and contains(@name, 'credentials.passcode') and contains(@autocomplete, 'off')]"

XPATH_OTP_PAGE_BUTTON_VERIFY_ELEMENT = "//input[contains(@type, 'submit') and contains(@value, 'Verify') and contains(@data-type, 'save')]"


# Predefined XPATHs for elements for the my profile page

XPATH_MY_PROFILE_PAGE_HEADER_ELEMENT = "//h2[contains(text(), 'My Profile')]"

XPATH_MY_PROFILE_P_HELLO_ELEMENT = "//p[starts-with(text(),'Hello,')]"

XPATH_MY_PROFILE_TABLE_ELEMENT = "//table[@id='desc']"

XPATH_MY_PROFILE_BUTTON_SIGN_OUT_ELEMENT = "//button[contains(@type, 'submit') and contains(text(), 'Sign out')]" 

XPATH_MY_PROFILE_BUTTON_INPUT_SCORE_ELEMENT = "//button[contains(text(), 'Input score')]"

XPATH_MY_PROFILE_TABLE_DATA_COLUMS_ELEMENT = "//table[contains(@id, 'desc')]//td"


# Predefined function that contain selenium web driver configuration

@pytest.fixture
def driver(selenium):
    
    selenium.get(URL_LOGIN_PAGE)
    
    time.sleep(1)
    
    ac = ActionChains(selenium)
    
    username_input = selenium.find_element(By.XPATH, XPATH_LOGIN_PAGE_INPUT_USERNAME_ELEMENT)
    
    ac.move_to_element(username_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(username_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(username_input).click().send_keys(USERNAME).perform()
    
    time.sleep(1)
    
    password_input = selenium.find_element(By.XPATH, XPATH_LOGIN_PAGE_INPUT_PASSWORD_ELEMENT)
    
    ac.move_to_element(password_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(password_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(password_input).click().send_keys(PASSWORD).perform()
    
    time.sleep(1)
    
    signin_button = selenium.find_element(By.XPATH, XPATH_LOGIN_PAGE_BUTTON_SIGN_IN_ELEMENT)
    
    ac.move_to_element(signin_button).perform()
    
    time.sleep(1)
    
    ac.move_to_element(signin_button).click().perform()
    
    time.sleep(2)
    
    otp_input = selenium.find_element(By.XPATH, XPATH_OTP_PAGE_INPUT_ENTER_CODE_ELEMENT)
    
    ac.move_to_element(otp_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(otp_input).click().perform()
    
    time.sleep(1)
    
    ac.move_to_element(otp_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(otp_input).click().send_keys(get_current_otp()).perform()
    
    time.sleep(1)
    
    verify_button = selenium.find_element(By.XPATH, XPATH_OTP_PAGE_BUTTON_VERIFY_ELEMENT)
    
    ac.move_to_element(verify_button).perform()
    
    time.sleep(1)
    
    ac.move_to_element(verify_button).click().perform()
    
    time.sleep(3)
    
    yield selenium


# Predefined functions for checking elements for the OTP verification page


# Check the URL of the my profile page
def my_profile_page_check_url(web_driver):
    
    assert URL_MY_PROFILE_PAGE in web_driver.current_url


# Check the header element of the at my profile page
def my_profile_page_check_header_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_MY_PROFILE_PAGE_HEADER_ELEMENT)


# Check the my profile header at my profile page
def my_profile_page_check_header_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_MY_PROFILE_PAGE_HEADER_ELEMENT)


# Check the 'Hello,' text at my profile page
def my_profile_page_check_p_hello_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_MY_PROFILE_P_HELLO_ELEMENT)


# Check the table element at my profile page
def my_profile_page_check_table_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_MY_PROFILE_TABLE_ELEMENT)


# Check the sign out button element at my profile page
def my_profile_page_check_button_sign_out_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_MY_PROFILE_BUTTON_SIGN_OUT_ELEMENT)


# Check the input score button element at my profile page
def my_profile_page_check_button_input_score_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_MY_PROFILE_BUTTON_INPUT_SCORE_ELEMENT)


# Predefined functions for getting the OTP code
def get_current_otp() -> str:
    
    totp = pyotp.TOTP(OTP_SECRET)
    
    return totp.now()


# Unit tests for the my profile page


def test_url_my_profile_page(driver):
    
    my_profile_page_check_url(driver)


def test_my_profile_page_check_header_element(driver):
    
    my_profile_page_check_header_element(driver)


def test_my_profile_page_check_p_hello_element(driver):
    
    my_profile_page_check_p_hello_element(driver)


def test_my_profile_page_check_table_element(driver):
        
    my_profile_page_check_table_element(driver)


def test_my_profile_page_check_button_sign_out_element(driver):
    
    my_profile_page_check_button_sign_out_element(driver)


def test_my_profile_page_check_button_input_score_element(driver):
    
    my_profile_page_check_button_input_score_element(driver)


# Test case for the my profile page suite

# Validate the my profile page
def test_validate_my_profile_page_suite(driver):
    
    print("start testing test_validate_my_profile_page_suite\n")

    my_profile_page_check_url(driver)
    
    my_profile_page_check_header_element(driver)
    
    my_profile_page_check_p_hello_element(driver)
    
    my_profile_page_check_table_element(driver)
    
    my_profile_page_check_button_sign_out_element(driver)
    
    my_profile_page_check_button_input_score_element(driver)
    
    print("\nend testing test_validate_my_profile_page_suite")