
from Pages.Tensor_page import PageUser

def test_Tensor_page(browser):
    Tensor_page = PageUser(browser)
    # Tensor_page.go_to_site()
    Tensor_page.check_people_power()

    Tensor_page.click_on_the_ABOUT()
    Tensor_page.check_img_size()