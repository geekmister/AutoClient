"""
@Project : cd-auto-test-client.git
@File    : sample_case.py
@IDE     : vscode
@Author  : geek mister
@Date    : 2024/3/14 15:56
@MyHome  : https://code.kp-para.cn/qa/cd-auto-test-client
@Desc    : todo
"""


from test_cases.base_case import BaseCase
from components.top_bar_component import TopBarComponent
from selenium import webdriver 


class SampleCase(BaseCase):
    """
    The sample case for the test.
    """
    
    def __init__(self):
        super().__init__()

    def test_login(self):
        """
        The sample case for the test.
        """

        driver = webdriver.Chrome()
        driver.get("https://keepwork.com/")

        top_bar_compoent = TopBarComponent(driver=driver)
        top_bar_compoent.click_login()
        pass


if __name__ == '__main__':
    sample_case = SampleCase()
    sample_case.test_login()