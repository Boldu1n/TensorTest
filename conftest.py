import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

download_path = os.getcwd()+"\\tests"

chrome_options = Options()
chrome_options.add_argument("--allow-running-insecure-content")  # Allow insecure content
chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://example.com")  # Replace example.com with your site's domain
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()