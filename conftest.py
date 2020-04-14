import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Добавляем возможность задать браузер при запуске тестов из консоли
    parser.addoption('--browser-name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome or firefox')

    # Добавляем возможность задать язык браузера при запуске тестов из консоли
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: ru, en, ... (etc.)")

    # parser.addoption('--product-name',
    #                  action='store',
    #                  help='Choose product name (book title)')
    #
    # parser.addoption('--product-price',
    #                  action='store',
    #                  help='Choose product price like 99,99 $')


@pytest.fixture(scope="function")
def browser(request):
    # Переменная имя браузера
    browser_name = request.config.getoption("browser_name")

    # Переменная язык, выбранный юзером
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)

        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(7)
    yield browser

    print("\nquit browser..")
    browser.quit()


# @pytest.fixture(scope="function")
# def product_name(request):
#     product_name = request.config.getoption("product_name")
#     yield product_name
#
#
# @pytest.fixture(scope="function")
# def product_price(request):
#     product_price = request.config.getoption("product_price")
#     yield product_price
