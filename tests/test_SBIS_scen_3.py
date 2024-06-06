import os
import shutil
import time
import math
from Pages.SBIS_page import PageUser

import glob

tmp_download_dir = os.getcwd() + "\\tests"
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0 Б"
   size_name = ("Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ", "ЭБ", "ЗБ", "ЁБ")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


def wait_until_download(timeout = 10):
    timeout_second = 0
    while os.path.exists(f'{tmp_download_dir}\\*.crdownload') or timeout_second<=timeout:
        time.sleep(1)
        timeout_second+=1
    if timeout_second==timeout:
        return 'файл загружается слишком долго'
    else:
        return 'файл загружен'
def get_download_size():
    return os.path.getsize(tmp_download_dir+"\\sbisplugin-setup-web.exe")

def check_size(download_size,web_size):
    return download_size in web_size
def test_download_loc_version(browser):
    SBIS_page = PageUser(browser)
    SBIS_page.go_to_site()
    SBIS_page.scroll_to_end()
    SBIS_page.click_lockal_version()
    # time.sleep(30)
    SBIS_page.click_plagin()
    SBIS_page.download_plagin()
    wait_until_download()
    download_size = get_download_size()
    download_size = convert_size(download_size)
    assert check_size(download_size,SBIS_page.Web_download_size)