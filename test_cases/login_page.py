"""
@Author  : Geekmister
@Date    : 2024/05/21 11:13
@MyHome  : https://github.com/geekmister
@Desc    : 
    Test case of login_page.py
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

import toolkits.driver_manager as driver_manager
from utils.logger import logger


chrome_options = driver_manager.ChromeOptions()
# webdriver = driver_manager.get_webdriver(options=chrome_options)
webdriver = webdriver.Chrome(options=chrome_options)


def setup_module(module):
    """
    Desc:
        Setup module. It will be executed before the first test function in the module.
    Args:
        module(Any): To point self module.
    Return:
        None
    """

    webdriver.get("http://www.keepwork.com")
    print(module.__name__ + " setup_module")


def teardown_module(module):
    """
    Desc:
        Teardown module. It will be executed after the last test function in the module.
    Args:
        module(Any): To point self module.
    Return:
        None
    """

    webdriver.quit()
    print(module.__name__ + " teardown_module")


def test_open_login_dialog():
    """
    Desc:
        Test open login dialog.
    Args:
        None
    Return:
        None
    """
 
    time.sleep(5)
    webdriver.find_element(By.XPATH, "/html/body/div[2]/section/header/div/ul/li[2]/button[2]").click()
    # wait = WebDriverWait(webdriver, 10)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div[1]/form/div[3]/div/button/span")))
    time.sleep(5)
    element_tem = webdriver.find_element(By.CLASS_NAME, "login-page-form-three-login")
    # dom = element_tem.get_attribute("outerHTML")
    # list = webdriver.find_elements(By.XPATH, "/html/body/div[5]/div/div/div/div/div[1]/form/div[3]/div/button/span")
    time.sleep(10)