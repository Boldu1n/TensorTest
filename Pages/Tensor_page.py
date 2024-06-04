from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
class TensorLocators:
    PEOPLE_POWER = (By.XPATH,'//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div')
    ABOUT = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    WORKING = (By.XPATH,'//*[@id="container"]/div[1]/div/div[4]')
    WORKING_IMG = (By.CSS_SELECTOR,'.tensor_ru-About__block3-image.new_lazy.loaded')

Tensor_url = "https://tensor.ru/"
class PageUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = Tensor_url

    def click_on_the_ABOUT(self):
        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])
        return self.click_element(TensorLocators.ABOUT,time=2)

    def check_people_power(self):
        try:
            people_power = self.find_element(TensorLocators.PEOPLE_POWER,time=2)
            assert people_power != None
        except:
            raise NoSuchElementException("""No block "Power in people""")
        return True

    def check_img_size(self):
        print()
        working = self.find_element(TensorLocators.WORKING,time=2)
        ActionChains(self.driver).scroll_to_element(working).perform()
        all_img = self.find_elements(TensorLocators.WORKING_IMG, time=2)
        img_size = all_img[0].size
        for img in all_img:
            print("Current img size: ",img.size)
            if img.size != img_size:
                raise ValueError("Different img size: %s , %s ",(img.size,img_size))
        return True