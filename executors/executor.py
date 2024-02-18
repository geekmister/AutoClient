"""
@Project : cd-auto-test-client.git
@File    : executor.py
@IDE     : PyCharm
@Author  : geek mister
@Date    : 2024/1/9 17:01
@MyHome  : https://github.com/geekmister
@Desc    : Test case executors
"""


class TestCaseExecutor:
    """

    """

    @staticmethod
    def execute(test_cases):
        for test_case in test_cases:
            handler(test_case)


def handler(test_case):
    # Handle test_info
    test_infos = test_case["test_infos"]
    handle_test_infos(test_infos)

    # Handle test_pres
    test_pres = test_case["test_pres"]

    # Handle test_steps
    test_steps = test_case["test_steps"]

    # Handle test_checks
    test_checks = test_case["test_checks"]


def handle_test_infos(test_infos):
    if test_infos.length > 0:
        test_info = test_infos[0]
        id = test_info["id"]
        check = test_info["check"]
        pre = test_info["pre"]


def handle_test_pres(test_pres):
    if test_pres.length > 0:
        for test_pre in test_pres:
            operate_parser(test_pre)


def handle_test_steps(test_pres):
    pass


def handle_test_checks(test_pres):
    pass


def operate_parser(item):
    """
    Operate parser, we
    Args:
        item(dict): item of test_pres & test_steps & test_checks

    Returns:
        None
    """

    operate_type = item["operate_type"]
    match operate_type:
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
        case "actions":
            operate_action = item["operate_action"]
            match operate_action:
                case "keyboard":
                    pass
                case "mouse":
                    pass
                case "pen":
                    pass
                case "wheel":
                    pass
                case _:
                    pass
            pass
        case _:
            pass
