# PythonQAAutomation
Python QA Tests Automation

First, please install Python version 3.10, you may refer to [python.org](https://www.python.org/)

Clone this repository by using the following command in your terminal or command prompt

`git clone https://github.com/dragon28/PythonQAAutomation.git`

then change directory

`cd PythonQAAutomation`

###### Install the following Python libraries:

* selenium
* pytest
* pytest-html
* pytest-print
* pytest-bdd
* pytest-selenium
* pytest-selenium-auto
* allure-pytest
* pyotp
* hypothesis

`pip install -r requirements.txt`

or

`pip install -r frezeed_requirements.txt`

**Note: For better compatibility use `pip install -r frezeed_requirements.txt`

Once done installing the Python libraries, we can run the Python program or script.

###### Example of Usage:

`python run_all_pytest-selenium_tests.py`

or

`python run_all_hypothesis_tests.py`

or

`pytest --driver Chrome`

or

`pytest --driver Chrome tests/hypothesis/test_sample_form_page_using_hypothesis.py`

or

`pytest --driver Chrome tests/pytest-selenium/test_otp_page.py::test_otp_page_verify_with_correct_code`

###### Report Directory:


