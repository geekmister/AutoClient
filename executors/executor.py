"""
@Project : cd-auto-test-client.git
@File    : executor.py
@IDE     : PyCharm
@Author  : geek mister
@Date    : 2024/1/9 17:01
@MyHome  : https://github.com/geekmister
@Desc    : Test case executor.
"""

from selenium.webdriver.common.by import By

from drivers import *


class TestCaseExecutor:
    """
    Test case executor class
    """

    __driver_manager = None
    __webdriver = None

    def __init__(self, test_cases):
        self.test_cases = test_cases

    def execute(self):
        """
        Main execute function
        Args:

        Returns:
            -> None
        """

        for test_case in self.test_cases:
            self.parser_test_infos(test_case["test_infos"])
            self.parser_test_pres(test_case["test_pres"])
            self.parser_test_steps(test_case["test_steps"])
            self.parser_test_checks(test_case["test_checks"])

    def execute_test_infos(self, test_infos):
        """
        Execute test info list
        Args:
            test_infos(list): list, test info list

        Returns:
            -> None
        """

        if len(test_infos) > 0:
            for test_info in test_infos:
                id = test_info["id"]
                check = test_info["check"]
                pre = test_info["pre"]

    def execute_test_pres(self, test_pres):
        """
        Execute test pre list
        Args:
            test_pres(list): list, test pre list

        Returns:
            -> None
        """

        if len(test_pres) > 0:
            for test_pre in test_pres:
                self.parser_operation_type(test_pre)

    def execute_test_steps(self, test_steps):
        """
        Execute test step list
        Args:
            test_steps(list): list, test step list

        Returns:
            -> None
        """

        pass

    def execute_test_checks(self, test_checks):
        """
        Execute test check list
        Args:
            test_checks(list): list, test check list

        Returns:
            -> None
        """

        pass

    def execute_operation_type(self, item):
        """
        Execute operation type
        Args:
            item(object): object, item object

        Returns:
            -> None
        """

        operation_type = item["operation_type"]
        match operation_type:
            case "driver":
                self.execute_operation_for_driver(item)
            case "browser":
                pass
            case "wait":
                pass
            case "element":
                pass
            case "interaction":
                pass
            case "interface":
                pass
            case "double-protocol":
                pass
            case "additional":
                pass
            case "trouble-removal":
                pass
            case _:
                pass

    def execute_operation_for_driver(self, item):
        """
        Execute operation for driver
        Args:
            item(object): object, item object

        Returns:
            -> None
        """

        local_or_remote = item["local_or_remote"]
        if local_or_remote == "local":
            operation_action = item["operation_action"]
            if operation_action == "open_url":
                browser_type = item["browser_type"]
                if browser_type == "chrome":
                    chrome_options = ChromeOptions()
                    self.__driver_manager = DriverManager(chrome_options, item["url"])
                    self.__webdriver = self.__driver_manager.get()

        else:
            # TODO remote drvier operation
            pass

    def execute_operation_for_wait(self, item):
        second = item["second"]
        find_element_way = item["find_element_way"]
        find_element_value = item["find_element_value"]

        if find_element_way == "id":
            element = self.__webdriver.find_element(By.id, item["find_element_value"])
        else:
            pass
