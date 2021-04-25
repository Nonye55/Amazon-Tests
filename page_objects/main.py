from config import WebDrivers
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as econ
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from variables import bar


class Amazon:
    def __init__(self):
        self.web = WebDrivers("Dogged")
        self.wait = WebDriverWait(self.web.driver, 80)

    def load_ama_page(self):
        self.web.driver.maximize_window()
        self.web.load_page(bar.amazon_page)

    def search_products(self):
        self.wait.until(econ.visibility_of_element_located((By.XPATH, bar.search_bar)))
        self.web.driver.find_element_by_xpath(bar.search_bar).send_keys(bar.product_name)
        self.web.driver.find_element_by_xpath(bar.search_button).click()
        self.wait.until(econ.element_located_to_be_selected((By.XPATH, bar.click_image)))
        self.web.driver.find_element_by_xpath(bar.click_image)
        self.wait.until(econ.element_to_be_clickable((By.XPATH, bar.Buy_now)))

    def buy_now(self):
        self.web.driver.find_element_by_xpath(bar.Buy_now).click()

    def close_page(self):
        self.web.driver.quit()


# web.get(bar.amazon_page)

# print("wfdcdcdf")
# wait.until(econ.visibility_of_element_located((By.XPATH, bar.search_bar)))
# print("not found")
# web.find_element_by_xpath(bar.search_bar).send_keys(bar.product_name)
# print("pass_here")
# web.find_element_by_xpath(bar.search_button).click()
# print("i passed is")
# wait.until(econ.element_located_to_be_selected((By.XPATH, bar.click_image)))
# print("am still here")
# web.find_element_by_xpath(bar.click_image).click()
# print("passed")
# wait.until(econ.element_to_be_clickable((By.XPATH, bar.Buy_song)))
# web.find_element_by_xpath(bar.Buy_song).click()
# print("am here")
# wait.until(econ.visibility_of_element_located((By.XPATH, bar.continue_to_checkout)))
# print("iihygygh")
# web.find_element_by_xpath(bar.continue_to_checkout).click()
# web.quit()
