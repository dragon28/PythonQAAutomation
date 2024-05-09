import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


# Predefined configuration

URL_SAMPLE_FORM_PAGE = "https://spa4h429l.otpyrc.dev/form"

SAMPLE_FORM_TEST_NAME = "Test Name"

SAMPLE_FORM_TEST_EMAIL = "testing123@testing123.test"

SAMPLE_FORM_TEST_SCORE = "80"

SAMPLE_FORM_TEST_ROLE = "Helper"


# Predefined XPATHs for elements for the sample form page

XPATH_SAMPLE_FORM_HEADER_ELEMENT = "//h4[@id='myModalLabel']"

XPATH_SAMPLE_FORM_INPUT_FORM_ELEMENT = "//form[contains(@role, 'form') and contains(@method, 'POST') and contains(@action, 'form')]"

XPATH_SAMPLE_FORM_LABEL_NAME_ELEMENT = "//label[contains(@for, 'name') and contains(text(), 'Name:')]"

XPATH_SAMPLE_FORM_INPUT_NAME_ELEMENT = "//input[contains(@id, 'name') and contains(@type, 'text') and contains(@name, 'name')]"

XPATH_SAMPLE_FORM_LABEL_EMAIL_ELEMENT = "//label[contains(@for, 'email') and contains(text(), 'Email:')]"

XPATH_SAMPLE_FORM_INPUT_EMAIL_ELEMENT = "//input[contains(@id, 'email') and contains(@type, 'email') and contains(@name, 'email')]"

XPATH_SAMPLE_FORM_LABELSCORE_ELEMENT = "//label[contains(@for, 'score') and contains(text(), 'Score:')]"

XPATH_SAMPLE_FORM_INPUT_SCORE_ELEMENT = "//input[contains(@id, 'number') and contains(@type, 'number') and contains(@name, 'score')]"

XPATH_SAMPLE_FORM_LABEL_ROLE_ELEMENT = "//label[contains(@for, 'role') and contains(text(), 'Role:')]"

XPATH_SAMPLE_FORM_SELECT_ROLE_ELEMENT = "//select[contains(@id, 'role')]"

XPATH_SAMPLE_FORM_BUTTON_SUBMIT_ELEMENT = "//button[contains(@type, 'submit') and contains(text(), 'Submit')]"


# Predefined XPATHs for elements for the submitted sample form page

XPATH_SUBMITTED_SAMPLE_FORM_HEADER_ELEMENT = "//h2[contains(text(), 'Thanks, here is what you have submitted:')]"

XPATH_SUBMITTED_SAMPLE_FORM_P_NAME_ELEMENT = "//p[contains(text(), 'Name:')]"

XPATH_SUBMITTED_SAMPLE_FORM_P_EMAIL_ELEMENT = "//p[contains(text(), 'Email:')]"

XPATH_SUBMITTED_SAMPLE_FORM_P_SCORE_ELEMENT = "//p[contains(text(), 'Score:')]"

XPATH_SUBMITTED_SAMPLE_FORM_P_ROLE_ELEMENT = "//p[contains(text(), 'Role:')]"


# Predefined function that contain selenium web driver configuration 

@pytest.fixture
def driver(selenium):
    
    selenium.get(URL_SAMPLE_FORM_PAGE)
    
    time.sleep(1)
    
    yield selenium


# Predefined functions for checking elements for the sample form page


# Check the URL of the sample form page
def sample_form_page_check_url(web_driver):
    
    assert URL_SAMPLE_FORM_PAGE in web_driver.current_url


# Check for header element at sample form page
def sample_form_page_check_header_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_HEADER_ELEMENT)


# Check for input form element at sample form page
def sample_form_page_check_input_form_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_INPUT_FORM_ELEMENT)


# Check for label name element at sample form page
def sample_form_page_check_label_name_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_LABEL_NAME_ELEMENT)


# Check for input name element at sample form page
def sample_form_page_check_input_name_element(web_driver):

    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_INPUT_NAME_ELEMENT)


# Check for label email element at sample form page
def sample_form_page_check_label_email_element(web_driver):
        
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_LABEL_EMAIL_ELEMENT)


# Check for input email element at sample form page
def sample_form_page_check_input_email_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_INPUT_EMAIL_ELEMENT)


# Check for label score element at sample form page
def sample_form_page_check_label_score_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_LABELSCORE_ELEMENT)


# Check for input score element at sample form page
def sample_form_page_check_input_score_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_INPUT_SCORE_ELEMENT)


# Check for label role element at sample form page
def sample_form_page_check_label_role_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_LABEL_ROLE_ELEMENT)


# Check for select role element at sample form page
def sample_form_page_check_select_role_element(web_driver):
    
    assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_SELECT_ROLE_ELEMENT)


# Check for button submit element at sample form page
def sample_form_page_check_button_submit_element(web_driver):
        
        assert web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_BUTTON_SUBMIT_ELEMENT)


# Predefined function for filling up the form and submit at sample form page
def sample_form_page_filling_up_form_and_submit(web_driver, name, email, score, role):
    
    ac = ActionChains(web_driver)
    
    name_input = web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_INPUT_NAME_ELEMENT)
    
    ac.move_to_element(name_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(name_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(name_input).click().send_keys(name).perform()
    
    time.sleep(1)
    
    email_input = web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_INPUT_EMAIL_ELEMENT)

    ac.move_to_element(email_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(email_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(email_input).click().send_keys(email).perform()
    
    time.sleep(1)
    
    score_input = web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_INPUT_SCORE_ELEMENT)
    
    ac.move_to_element(score_input).perform()
    
    time.sleep(1)
    
    ac.move_to_element(score_input).click().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
    
    time.sleep(1)
    
    ac.move_to_element(score_input).click().send_keys(score).perform()
    
    time.sleep(1)
    
    role_select_input = web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_SELECT_ROLE_ELEMENT)
    
    role_select = Select(role_select_input)
    
    ac.move_to_element(role_select_input).perform()
    
    time.sleep(1)
    
    role_select.select_by_value(role)
    
    time.sleep(1)
    
    submit_button = web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_BUTTON_SUBMIT_ELEMENT)
    
    ac.move_to_element(submit_button).perform()
    
    time.sleep(1)
    
    ac.move_to_element(submit_button).click().perform()
    
    time.sleep(2)
    
    return web_driver


# Unit tests for the sample form page


def test_url_sample_form_page(driver):
    
    sample_form_page_check_url(driver)


def test_sample_form_page_check_header_element(driver):
    
    sample_form_page_check_header_element(driver)


def test_sample_form_page_check_input_form_element(driver):
    
    sample_form_page_check_input_form_element(driver)


def test_sample_form_page_check_label_name_element(driver):
        
    sample_form_page_check_label_name_element(driver)


def test_sample_form_page_check_input_name_element(driver):
    
    sample_form_page_check_input_name_element(driver)


def test_sample_form_page_check_label_email_element(driver):
    
    sample_form_page_check_label_email_element(driver)


def test_sample_form_page_check_input_email_element(driver):
    
    sample_form_page_check_input_email_element(driver)


def test_sample_form_page_check_label_score_element(driver):
    
    sample_form_page_check_label_score_element(driver)


def test_sample_form_page_check_input_score_element(driver):
    
    sample_form_page_check_input_score_element(driver)


def test_sample_form_page_check_label_role_element(driver):
    
    sample_form_page_check_label_role_element(driver)

   
def test_sample_form_page_check_select_role_element(driver):
    
    sample_form_page_check_select_role_element(driver)


def test_sample_form_page_check_button_submit_element(driver):
    
    sample_form_page_check_button_submit_element(driver)


# Test cases based on scenarios


# Validate the sample form page
def test_validate_sample_form_page_suite(driver):
    
    print("start testing test_validate_sample_form_page_suite\n")
    
    sample_form_page_check_url(driver) 
    
    sample_form_page_check_header_element(driver)
    
    sample_form_page_check_input_form_element(driver)
    
    sample_form_page_check_label_name_element(driver)
    
    sample_form_page_check_input_name_element(driver)
    
    sample_form_page_check_label_email_element(driver)
    
    sample_form_page_check_input_email_element(driver)
    
    sample_form_page_check_label_score_element(driver)
    
    sample_form_page_check_input_score_element(driver)
    
    sample_form_page_check_label_role_element(driver)
    
    sample_form_page_check_select_role_element(driver)
    
    sample_form_page_check_button_submit_element(driver)
    
    print("\nend testing test_validate_sample_form_page_suite")


# Test case for submitting the form with empty information or details
@pytest.mark.parametrize("name, email, score, role",
                         [
                            pytest.param("", "", "", "", marks=pytest.mark.xfail(reason="Role Select Input Unable to Handle Null or Empty Value by default"))
                         ]
                         )
def test_sample_form_page_form_with_empty_form(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_empty_form\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Sample Form" in web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_HEADER_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_empty_form")


# Test case for submitting the form with role but without name, email, and score
@pytest.mark.parametrize("name, email, score, role",
                         [
                            ("", "", "", SAMPLE_FORM_TEST_ROLE)
                         ]
                         )
def test_sample_form_page_form_with_empty_name_email_score(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_empty_name_email_score\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Sample Form" in web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_HEADER_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_empty_name_email_score")


# Test case for submitting the form with name and role but without email, score
@pytest.mark.parametrize("name, email, score, role",
                         [
                            (SAMPLE_FORM_TEST_NAME, "", "", SAMPLE_FORM_TEST_ROLE)
                         ]
                         )
def test_sample_form_page_form_with_empty_email_score(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_empty_email_score\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Sample Form" in web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_HEADER_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_empty_email_score")


# Test case for submitting the form with name, email and role but without score
@pytest.mark.parametrize("name, email, score, role",
                         [
                            (SAMPLE_FORM_TEST_NAME, SAMPLE_FORM_TEST_EMAIL, "", SAMPLE_FORM_TEST_ROLE)
                         ]
                         )
def test_sample_form_page_form_with_empty_score(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_empty_score\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Thanks, here is what you have submitted:" in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_HEADER_ELEMENT).text
    
    assert name in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_NAME_ELEMENT).text
    
    assert email in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_EMAIL_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_empty_score")


# Test case for submitting the form with name, email, score and role and validate all the submitted details
@pytest.mark.parametrize("name, email, score, role", 
                        [
                            pytest.param(SAMPLE_FORM_TEST_NAME, SAMPLE_FORM_TEST_EMAIL, SAMPLE_FORM_TEST_SCORE, SAMPLE_FORM_TEST_ROLE, 
                                        marks=pytest.mark.xfail(reason="[Bug] Submitted Role Select Value Was not Displayed")
                                        )
                        ]
                        )
def test_sample_form_page_form_with_full_details(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_full_details\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Thanks, here is what you have submitted:" in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_HEADER_ELEMENT).text
    
    assert name in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_NAME_ELEMENT).text
    
    assert email in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_EMAIL_ELEMENT).text
    
    assert score in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_SCORE_ELEMENT).text
    
    assert role in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_ROLE_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_full_details")


# Test case for submitting the form with all the details but without validating the submitted role information
@pytest.mark.parametrize("name, email, score, role", 
                        [
                            pytest.param(SAMPLE_FORM_TEST_NAME, SAMPLE_FORM_TEST_EMAIL, SAMPLE_FORM_TEST_SCORE, SAMPLE_FORM_TEST_ROLE)
                        ]
                        )
def test_sample_form_page_form_with_full_details_without_validate_submitted_role_detail(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_full_details_without_validate_submitted_role_detail\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Thanks, here is what you have submitted:" in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_HEADER_ELEMENT).text
    
    assert name in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_NAME_ELEMENT).text
    
    assert email in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_EMAIL_ELEMENT).text
    
    assert score in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_SCORE_ELEMENT).text
    
    # assert role in web_driver.find_element(By.XPATH, XPATH_SUBMITTED_SAMPLE_FORM_P_ROLE_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_full_details_without_validate_submitted_role_detail")


# Test case for submitting the form with full details but with wrong email format
@pytest.mark.parametrize("name, email, score, role", 
                        [
                            pytest.param(SAMPLE_FORM_TEST_NAME, SAMPLE_FORM_TEST_NAME, SAMPLE_FORM_TEST_SCORE, SAMPLE_FORM_TEST_ROLE)
                        ]
                        )
def test_sample_form_page_form_with_full_details_but_wrong_email_format(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_full_details_but_wrong_email_format\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Sample Form" in web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_HEADER_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_full_details_but_wrong_email_format")


# Test case for submitting the form with full details but with negative score
@pytest.mark.parametrize("name, email, score, role", 
                        [
                            pytest.param(SAMPLE_FORM_TEST_NAME, SAMPLE_FORM_TEST_EMAIL, "-1", SAMPLE_FORM_TEST_ROLE)
                        ]
                        )
def test_sample_form_page_form_with_full_details_but_with_negative_score(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_full_details_but_with_negative_score\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Sample Form" in web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_HEADER_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_full_details_but_with_negative_score")


# Test case for submitting the form with full details but with score over 100
@pytest.mark.parametrize("name, email, score, role", 
                        [
                            pytest.param(SAMPLE_FORM_TEST_NAME, SAMPLE_FORM_TEST_EMAIL, "300", SAMPLE_FORM_TEST_ROLE)
                        ]
                        )
def test_sample_form_page_form_with_full_details_but_with_score_over_100(driver, name, email, score, role):
    
    print("start testing test_sample_form_page_form_with_full_details_but_with_score_over_100\n")
    
    web_driver = sample_form_page_filling_up_form_and_submit(driver, name, email, score, role)
    
    assert "Sample Form" in web_driver.find_element(By.XPATH, XPATH_SAMPLE_FORM_HEADER_ELEMENT).text
    
    print("\nend testing test_sample_form_page_form_with_full_details_but_with_score_over_100")