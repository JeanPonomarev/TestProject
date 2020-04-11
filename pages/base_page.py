class BasePage:
    # конструктор
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # метод, отрывающий нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)
