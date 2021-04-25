from selenium import webdriver


class WebDrivers:
    def __init__(self, web):
        if web == "Dogged":
            self.driver = webdriver.Chrome()
        elif web == "SAF":
            self.driver = webdriver.Edge()
        else:
            print(f"{web} Not found")

    def load_page(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

