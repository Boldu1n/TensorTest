
import time

from Pages.SBIS_page import PageUser

OUR_REGION = "Республика Башкортостан"
CHANGED_REGION = "Камчатский край"


def test_SBIS_page_scen_2(browser):
    SBIS_page = PageUser(browser)
    SBIS_page.go_to_site()
    SBIS_page.click_on_the_CONTACTS()
    SBIS_page.check_region(OUR_REGION)
    SBIS_page.check_partners()
    SBIS_page.change_region(CHANGED_REGION)
    time.sleep(2)
    SBIS_page.check_region(CHANGED_REGION)
    SBIS_page.check_partners()
    SBIS_page.check_title(CHANGED_REGION)
    SBIS_page.check_url(CHANGED_REGION)
