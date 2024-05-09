import pytest


@pytest.fixture(scope='function')
def selenium(selenium):
    
    selenium.maximize_window()
    
    return selenium


def pytest_assertion_pass(item, lineno, orig, expl):
    
    print("asserting that {} | at Line {} | {} | {} | Pass\n".format(item, lineno, orig, expl))