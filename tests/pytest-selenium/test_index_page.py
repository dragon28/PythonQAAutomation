import pytest

from selenium.webdriver.common.by import By

import time


# Predefined configuration

URL_INDEX_PAGE = "https://spa4h429l.otpyrc.dev/"



# Predefined XPATHs for elements for the index page

XPATH_INDEX_PAGE_TITLE_ELEMENT = "//title"

XPATH_INDEX_PAGE_BODY_H1_ELEMENT = "//body/h1"

XPATH_INDEX_PAGE_P_WELCOME_TO_ELEMENT = "//p[contains(text(), 'Welcome to')]"

XPATH_INDEX_PAGE_FORM_SIGN_IN_ELEMENT = "//form[contains(@action, '/signin')]"

XPATH_INDEX_PAGE_BUTTON_SIGN_IN_ELEMENT = "//button[text()='Sign in']"

XPATH_INDEX_PAGE_FORM_INPUT_SCORE_ELEMENT = "//form[contains(@action, '/form')]"

XPATH_INDEX_PAGE_BUTTON_INPUT_SCORE_ELEMENT = "//button[text()='Input score']"


# Predefined XPATHs for elements for the login page

XPATH_LOGIN_PAGE_HEADER_SIGN_IN_ELEMENT = "//h2[contains(@class, 'okta-form-title o-form-head')]"


# Predefined XPATHs for elements for the sample form page

XPATH_SAMPLE_FORM_HEADER_ELEMENT = "//h4[@id='myModalLabel']"


# Predefined function that contain selenium web driver configuration 

@pytest.fixture
def driver(selenium):
    
    selenium.get(URL_INDEX_PAGE)
    
    yield selenium


# Predefined functions for checking elements for the index page


# Check the URL of the index page
def index_page_check_url(web_driver):
    
    assert web_driver.current_url in URL_INDEX_PAGE


# Check the 'Welcome to' text in the index page
def index_page_check_p_welcome_to_element(web_driver):
    
     assert web_driver.find_element(By.XPATH, XPATH_INDEX_PAGE_P_WELCOME_TO_ELEMENT).text == 'Welcome to'


# Check the form element that allow sign in at index page
def index_page_check_form_sign_in_element(web_driver):
    
    assert "/signin" in web_driver.find_element(By.XPATH, XPATH_INDEX_PAGE_FORM_SIGN_IN_ELEMENT).get_dom_attribute('action')


# Check for sign in button element at index page
def index_page_check_button_sign_in_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_INDEX_PAGE_BUTTON_SIGN_IN_ELEMENT).text == 'Sign in'


# Check the form element that allow input score at index page
def index_page_check_form_input_score_element(web_driver):
    
    assert "/form" in web_driver.find_element(By.XPATH, XPATH_INDEX_PAGE_FORM_INPUT_SCORE_ELEMENT).get_dom_attribute('action')


# Check for input score button element at index page
def index_page_check_button_input_score_element(web_driver):
        
    assert "Input score" in web_driver.find_element(By.XPATH, XPATH_INDEX_PAGE_BUTTON_INPUT_SCORE_ELEMENT).text


# Check for title element is not empty at the index page
def index_page_check_title_element(web_driver):
        
    assert web_driver.find_element(By.XPATH, XPATH_INDEX_PAGE_TITLE_ELEMENT).text != ""


# Check for body header 1 element is not empty at the index page
def index_page_check_body_h1_element(web_driver):
        
    assert web_driver.find_element(By.XPATH, XPATH_INDEX_PAGE_BODY_H1_ELEMENT).text != ""


# Check the header sign in element at login page
def login_page_check_header_sign_in_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_HEADER_SIGN_IN_ELEMENT).text in 'Sign In'


# Check for header elemnt at sample form page
def sample_form_check_header_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_HEADER_ELEMENT).text in 'Sample Form'


# Unit tests for the index page


def test_url_index_page(driver):
    
    index_page_check_url(driver)
 
   
def test_index_page_check_p_welcome_to_element(driver):
    
    index_page_check_p_welcome_to_element(driver)


def test_index_page_check_form_sign_in_element(driver):
    
    index_page_check_form_sign_in_element(driver)


def test_index_page_check_button_sign_in_element(driver):
    
    index_page_check_button_sign_in_element(driver)


def test_index_page_check_form_input_score_element(driver):
    
    index_page_check_form_input_score_element(driver)


def test_index_page_check_button_input_score_element(driver):
    
    index_page_check_button_input_score_element(driver)


@pytest.mark.xfail(reason="Page Title is Empty without any text")
def test_index_page_check_title_element(driver):
    
    index_page_check_title_element(driver)


@pytest.mark.xfail(reason="Body Header 1 Text is Empty without any text")
def test_index_page_check_body_h1_element(driver):
    
    index_page_check_body_h1_element(driver)


# Test Cases based on scenarios

# Validate the index page
def test_validate_index_page_suite(driver):
    
    print("start testing test_validate_index_page_suite\n")

    index_page_check_url(driver)

    index_page_check_p_welcome_to_element(driver)
    
    index_page_check_form_sign_in_element(driver)
    
    index_page_check_button_sign_in_element(driver)
    
    index_page_check_form_input_score_element(driver)
    
    index_page_check_button_input_score_element(driver)
    
    print("\nend testing test_validate_index_page_suite")


# Test Case on clicking the sign in button
def test_index_page_click_sign_in_button(driver):
    
    print("start testing test_index_page_click_sign_in_button\n")
    
    driver.find_element(By.XPATH, XPATH_INDEX_PAGE_BUTTON_SIGN_IN_ELEMENT).click()
    
    time.sleep(2)
    
    assert 'okta.com' in driver.current_url
    
    login_page_check_header_sign_in_element(driver)
    
    print("\nend testing test_index_page_click_sign_in_button")


# Test Case on clicking the input score button
def test_index_page_click_input_score_button(driver):
    
    print("start testing test_index_page_click_input_score_button\n")
    
    driver.find_element(By.XPATH, XPATH_INDEX_PAGE_BUTTON_INPUT_SCORE_ELEMENT).click()
    
    time.sleep(2)
    
    assert str(URL_INDEX_PAGE + 'form') in driver.current_url
    
    sample_form_check_header_element(driver)
    
    print("\nend testing test_index_page_click_input_score_button")