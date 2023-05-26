import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    elif request.param == "edge":
        web_driver = webdriver.Edge()

    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()
