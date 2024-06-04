from Pages.SBIS_page import PageUser


def test_SBIS_page(browser):
    SBIS_page = PageUser(browser)
    SBIS_page.go_to_site()
    SBIS_page.click_on_the_CONTACTS()
    SBIS_page.click_on_the_TENSOR_BANNER()
