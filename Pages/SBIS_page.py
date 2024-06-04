from BaseApp import BasePage
from selenium.webdriver.common.by import By

class SBISLocators:
    CONTACTS = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a')
    TENSOR_BANNER = (By.XPATH,'//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')

SBIS_url = "https://sbis.ru/"

class PageUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = SBIS_url

    def click_on_the_TENSOR_BANNER(self):
        return self.click_element(SBISLocators.TENSOR_BANNER,time=2)

    def click_on_the_CONTACTS(self):
        return self.click_element(SBISLocators.CONTACTS,time=2)
