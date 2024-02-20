"""
@Project : cd-auto-test-client.git
@File    : executor.py
@IDE     : PyCharm
@Author  : geek mister
@Date    : 2024/1/9 17:01
@MyHome  : https://github.com/geekmister
@Desc    : Test case executor.
"""


class TestCaseExecutor:
    """
    Test case executor class
    """

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

            test_infos = test_case["test_infos"]
            self.parser_test_infos(test_infos)

            test_pres = test_case["test_pres"]
            self.parser_test_pres(test_pres)

            test_steps = test_case["test_steps"]
            self.parser_test_steps(test_steps)

            test_checks = test_case["test_checks"]
            self.parser_test_checks(test_checks)

    def parser_test_infos(self, test_infos):
        """
        Parser test info list
        Args:
            test_infos(list): list, test info list

        Returns:
            -> None
        """

        if test_infos.length > 0:
            test_info = test_infos[0]
            id = test_info["id"]
            check = test_info["check"]
            pre = test_info["pre"]

    def parser_test_pres(self, test_pres):
        """
        Parser test pre list
        Args:
            test_pres(list): list, test pre list

        Returns:
            -> None
        """

        if test_pres.length > 0:
            for test_pre in test_pres:
                self.parser_operation_type(test_pre)

    def parser_test_steps(self, test_steps):
        """
        Parser test step list
        Args:
            test_steps(list): list, test step list

        Returns:
            -> None
        """

        pass

    def parser_test_checks(self, test_checks):
        """
        Parser test check list
        Args:
            test_checks(list): list, test check list

        Returns:
            -> None
        """

        pass

    def parser_operation_type(self, item):
        """
        Parser operation type
        Args:
            item(object): object, item object

        Returns:
            -> None
        """

        operation_type = item["operation_type"]
        match operation_type:
            case "driver":
                pass
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