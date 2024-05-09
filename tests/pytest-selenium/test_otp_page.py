import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

import pyotp


# Predefined configuration

URL_LOGIN_PAGE = "https://spa4h429l.otpyrc.dev/signin"

USERNAME = "sengloong82@gmail.com"

PASSWORD = "CDCQATest123"

OTP_SECRET = "25TBJTZ3JDJPSZNC"

WRONG_CODE = "123456"


# Predefined XPATHs for elements for the login page

XPATH_LOGIN_PAGE_INPUT_USERNAME_ELEMENT = "//input[contains(@type, 'text') and contains(@name, 'identifier') and contains(@autocomplete, 'username')]"

XPATH_LOGIN_PAGE_INPUT_PASSWORD_ELEMENT = "//input[contains(@type, 'password') and contains(@name, 'credentials.passcode') and contains(@autocomplete, 'current-password') and contains(@class, 'password-with-toggle')]"

XPATH_LOGIN_PAGE_BUTTON_SIGN_IN_ELEMENT = "//input[contains(@type, 'submit') and contains(@value, 'Sign in') and contains(@data-type, 'save')]"


# Predefined XPATHs for elements for the OTP verification page

XPATH_OTP_PAGE_INPUT_FORM_ELEMENT = "//form[contains(@class, 'google-authenticator-challenge') and contains(@method, 'POST') and contains(@action, '/oauth2/default/v1/authorize')]"

XPATH_OTP_PAGE_HEADER_VERIFY_ELEMENT = "//h2[contains(text(), 'Verify with Google Authenticator')]"

XPATH_OTP_PAGE_LABEL_ENTER_CODE_ELEMENT = "//label[contains(text(), 'Enter code')]"

XPATH_OTP_PAGE_INPUT_ENTER_CODE_ELEMENT = "//input[contains(@type, 'text') and contains(@name, 'credentials.passcode') and contains(@autocomplete, 'off')]"

XPATH_OTP_PAGE_BUTTON_VERIFY_ELEMENT = "//input[contains(@type, 'submit') and contains(@value, 'Verify') and contains(@data-type, 'save')]"

XPATH_OTP_PAGE_SPAN_USERNAME_ELEMENT = "//span[contains(text(), '" + USERNAME + "')]"

XPATH_OTP_PAGE_LINK_BACK_TO_SIGN_IN_ELEMENT = "//a[contains(text(), 'Back to sign in')]"

XPATH_OTP_PAGE_P_ALERT_EMPTY_ELEMENT = "//p[contains(text(), 'This field cannot be left blank')]"

XPATH_OTP_PAGE_P_ALERT_FORM_ERROR_ELEMENT = "//p[contains(text(), 'We found some errors. Please review the form and make corrections.')]"

XPATH_OTP_PAGE_P_ALERT_CODE_ERROR_ELEMENT = '//p[contains(text(), "Your code doesn\'t match our records. Please try again.")]'


# Predefined XPATHs for elements for the my profile page

XPATH_MY_PROFILE_PAGE_HEADER_ELEMENT = "//h2[contains(text(), 'My Profile')]"

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
    
    time.sleep(3)
    
    yield selenium


# Predefined functions for checking elements for the OTP verification page

# Check the URL of the OTP verification page
def otp_page_check_url(web_driver):
    
    assert 'okta.com' in web_driver.current_url


# Check the input form element at the OTP verification page
def otp_page_input_check_input_form_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_INPUT_ENTER_CODE_ELEMENT)


# Check the header verify element at the OTP verification page
def otp_page_check_header_verify_element(web_driver):
        
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_HEADER_VERIFY_ELEMENT)


# Check the label enter code element at the OTP verification page
def otp_page_check_label_enter_code_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_LABEL_ENTER_CODE_ELEMENT)

# Check the input enter code element at the OTP verification page
def otp_page_check_input_enter_code_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_INPUT_ENTER_CODE_ELEMENT)

# Check the button verify element at the OTP verification page
def otp_page_check_button_verify_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_BUTTON_VERIFY_ELEMENT)


# Check the span username element at the OTP verification page
def otp_page_check_span_username_element(web_driver):
        
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_SPAN_USERNAME_ELEMENT)


# Check the link back to sign in element at the OTP verification page
def otp_page_check_link_back_to_sign_in_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_LINK_BACK_TO_SIGN_IN_ELEMENT)


# Predefined functions for getting the OTP code
def get_current_otp() -> str:
    
    totp = pyotp.TOTP(OTP_SECRET)
    
    return totp.now()

# Predefined functions for getting the data from table at my profile page
def get_my_profile_page_table_data(web_driver):
    
    data = []
    
    cols = web_driver.find_elements(By.XPATH, XPATH_MY_PROFILE_TABLE_DATA_COLUMS_ELEMENT)
    
    for col in cols:
        
        data.append(col.text)
    
    return data


# Predefined functions for filling up the OTP code and verify
def otp_page_filling_up_otp_code_and_verify(web_driver, otp_code):
    
    ac = ActionChains(web_driver)
    
    otp_input = web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_INPUT_ENTER_CODE_ELEMENT)
    
    ac.move_to_element(otp_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(otp_input).click().perform()
    
    time.sleep(1)
    
    ac.move_to_element(otp_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(otp_input).click().send_keys(otp_code).perform()
    
    time.sleep(1)
    
    verify_button = web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_BUTTON_VERIFY_ELEMENT)
    
    ac.move_to_element(verify_button).perform()
    
    time.sleep(1)
    
    ac.move_to_element(verify_button).click().perform()
    
    time.sleep(3)
    
    return web_driver


# Unit tests for the OTP verification page


def test_url_otp_page(driver):
    
   otp_page_check_url(driver)


def test_otp_page_check_input_form_element(driver):
    
    otp_page_input_check_input_form_element(driver)
    

def test_otp_page_check_header_verify_element(driver):
    
    otp_page_check_header_verify_element(driver)


def test_otp_page_check_label_enter_code_element(driver):
        
    otp_page_check_label_enter_code_element(driver)
    

def test_otp_page_check_input_enter_code_element(driver):
    
    otp_page_check_input_enter_code_element(driver)


def test_otp_page_check_button_verify_element(driver):
    
    otp_page_check_button_verify_element(driver)
    

def test_otp_page_check_span_username_element(driver):
    
    otp_page_check_span_username_element(driver)


def test_otp_page_check_link_back_to_sign_in_element(driver):
        
    otp_page_check_link_back_to_sign_in_element(driver)


# Test cases based on scenarios

# Validate the OTP verification page
def test_validate_otp_page_suite(driver):
    
    print("start testing test_validate_otp_page_suite\n")
    
    test_url_otp_page(driver)
    
    test_otp_page_check_input_form_element(driver)
    
    test_otp_page_check_header_verify_element(driver)
    
    test_otp_page_check_label_enter_code_element(driver)
    
    test_otp_page_check_input_enter_code_element(driver)
    
    test_otp_page_check_button_verify_element(driver)
    
    test_otp_page_check_span_username_element(driver)
    
    test_otp_page_check_link_back_to_sign_in_element(driver)
    
    print("\nend testing test_validate_login_page_suite")


# Test case for verifying the OTP with correct code
@pytest.mark.parametrize("otp", [pytest.param(get_current_otp())])
def test_otp_page_verify_with_correct_code(driver, otp):
    
    print("start testing test_otp_page_verify_with_correct_code\n")
    
    web_driver = otp_page_filling_up_otp_code_and_verify(driver, otp)
    
    data = get_my_profile_page_table_data(web_driver)
    
    assert '/profile' in web_driver.current_url
    
    assert 'My Profile' in web_driver.find_element(By.XPATH, XPATH_MY_PROFILE_PAGE_HEADER_ELEMENT).text
    
    assert USERNAME in data
    
    print("\nend testing test_otp_page_verify_with_correct_code")
    

# Test case for verifying the OTP with empty code
@pytest.mark.parametrize("otp", [pytest.param("")])
def test_otp_page_verify_with_empty_code(driver, otp):
    
    print("start testing test_otp_page_verify_with_empty_code\n")
    
    web_driver = otp_page_filling_up_otp_code_and_verify(driver, otp)
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_P_ALERT_EMPTY_ELEMENT)
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_P_ALERT_FORM_ERROR_ELEMENT)
    
    print("\nend testing test_otp_page_verify_with_empty_code")


# Test case for verifying the OTP with wrong code
@pytest.mark.parametrize("otp", [pytest.param(WRONG_CODE)])
def test_otp_page_verify_with_wrong_code(driver, otp):
    
    print("start testing test_otp_page_verify_with_wrong_code\n")
    
    web_driver = otp_page_filling_up_otp_code_and_verify(driver, otp)
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_P_ALERT_CODE_ERROR_ELEMENT)
    
    assert web_driver.find_element(By.XPATH, XPATH_OTP_PAGE_P_ALERT_FORM_ERROR_ELEMENT)
    
    print("\nend testing test_otp_page_verify_with_empty_code")