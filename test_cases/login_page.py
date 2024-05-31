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
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("--disable-infobars")
webdriver = driver_manager.get_webdriver(options=chrome_options)


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

    # NOTE 
    # The under code try...except...finally... is written by official document selenium-python, but it's running failed.
    # Annoted four lines is running success.
    # So, I need to learn to why write way official is failed. It's not undertand.
    try:
        element = WebDriverWait(webdriver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/section/header/div/ul/li[2]/button[2]")))
        element.click()
        element = WebDriverWait(webdriver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "forget-pwd")))
        assert True
    except Exception as e:
        logger.error("test_open_login_dialog error: %s", e)
        assert False
    finally:
        driver_manager.webdriver_quit(webdriver)
    
    # time.sleep(10)
    # webdriver.find_element(By.XPATH, "/html/body/div[2]/section/header/div/ul/li[2]/button[2]").click()
    # time.sleep(10)
    # assert webdriver.find_element(By.CLASS_NAME, "forget-pwd").text == "忘记密码?"