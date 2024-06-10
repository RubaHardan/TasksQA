import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=['chrome', 'firefox'])
def driver_init(request):
    if request.param == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--start-maximized')
        driver = webdriver.Firefox(options=firefox_options)

    yield driver
    driver.quit()