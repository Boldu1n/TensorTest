import os
import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By

import re

def transliteration_helper(text : str):
    mapping = {
        "щ": "shh", "ш": "sh", "ч": "ch", "ц": "cz", "ю": "yu", "я": "ya", "ё": "yo", "ж": "zh", "ъ": "`", "ы": "y`", "э": "e`",
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "з": "z", "и": "i", "й": "j", "к": "k", "л": "l", "м": "m",
        "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ь": "`"
    }

    text = text.lower().replace(" ", "-")
    for cyrillic, latin in mapping.items():
        text = re.sub(cyrillic, latin, text)

    return text.replace("`", "")




class SBISLocators:
    CONTACTS = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a')
    TENSOR_BANNER = (By.XPATH,'//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
    REGNAME = (By.XPATH,'//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    PARTNERS = (By.CSS_SELECTOR,'.sbisru-Contacts-List__item.sbisru-text--standart.sbisru-Contacts__text--500.pv-8.pv-xm-16.pl-24.pr-12.ph-xm-12.mb-xm-8.ws-flexbox.ws-justify-content-between.ws-align-items-start')
    LOCAL_VERSION = (By.XPATH,'//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')
    PLAGIN = (By.XPATH,'//div[@data-id="plugin"]')
    DOWNLOAD = (By.CSS_SELECTOR,'div.ws-SwitchableArea__item.ws-component.ws-enabled.ws-has-focus > div:nth-child(4) > div.sbis_ru-DownloadNew-flex__child.sbis_ru-DownloadNew-flex__child--width-1 > div > a')



SBIS_url = "https://sbis.ru/"

class PageUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = SBIS_url

    def click_on_the_TENSOR_BANNER(self):
        return self.click_element(SBISLocators.TENSOR_BANNER,time=2)

    def click_on_the_CONTACTS(self):
        return self.click_element(SBISLocators.CONTACTS,time=2)


    def check_region(self, region_name = "Ярославская область"):
        reg_name = self.find_element(SBISLocators.REGNAME,time=2).text
        print(reg_name,region_name)
        assert reg_name==region_name, """Регионы не совпадают"""

    def change_region(self, new_region: str = "Ярославская область"):
        self.click_element(SBISLocators.REGNAME,time=2)
        locator = (By.XPATH,f"//*[contains(text(), '{new_region}')]")
        return self.click_element(locator)



    def check_partners(self):
        partner_list = self.find_elements(SBISLocators.PARTNERS, time=2)
        assert len(partner_list)>0,"Список партнеров пуст"

    def check_url(self,reg_name):
        tranlate_reg_name = transliteration_helper(reg_name)
        print(tranlate_reg_name,self.driver.current_url)
        assert tranlate_reg_name in self.driver.current_url
        pass

    def check_title(self,reg_name):
        print(reg_name,self.driver.title)
        assert reg_name in self.driver.title,"Заголовок не совпадает с регионом"




    def scroll_to_end(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_lockal_version(self):
        return self.click_element(SBISLocators.LOCAL_VERSION,time=2)

    def click_plagin(self):
        time.sleep(2)
        return self.click_element(SBISLocators.PLAGIN,time=2)


    def download_plagin(self):
        # self.driver.set_preference("browser.download.dir", os.getcwd())
        self.Web_download_size = self.find_element(SBISLocators.DOWNLOAD,time=2).text
        self.click_element(SBISLocators.DOWNLOAD,time=2)

