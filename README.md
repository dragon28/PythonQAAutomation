# PythonQAAutomation
Python QA Tests Automation

Requirement:

First, please install Python version 3.10, you may refer to [python.org](https://www.python.org/)

Second, please install [Allure Rport](https://allurereport.org/), you may refer to [Install or upgrade Allure Report](https://allurereport.org/docs/install/)

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

For executing all the pytest-selenium tests:

`python run_all_pytest-selenium_tests.py`

or

For executing all the hypothesis tests:

`python run_all_hypothesis_tests.py`

or

`pytest --driver Chrome`

or

For executing specific test program file:

`pytest --driver Chrome tests/hypothesis/test_sample_form_page_using_hypothesis.py`

or

For executing specific test function inside the program file:

`pytest --driver Chrome tests/pytest-selenium/test_otp_page.py::test_otp_page_verify_with_correct_code`



**Note: You may find the test report inside the `reports` or `allure-report` directory or test log inside the `logs` directory

###### How to Generate Allure Report:

If you are using `pytest` command to execute the test, then you may want to use `allure generate --single-file allure-results --clean` commands to generate the Allure report.

Once the report was generated, it will be store in the `allure-report` directory


